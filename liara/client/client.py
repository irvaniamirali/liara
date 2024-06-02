from liara import errors

from typing import Optional

from os.path import exists
import requests
import json
import time


class Client:

    def __init__(
            self,
            name: str,
            token: Optional[str] = None,
            timeout: Optional[int] = 20,
            version: Optional[int] = 1
    ):
        self.token = token
        self.version = version
        self.timeout = timeout
        self.session = requests.session()

        if not token:
            if not exists(f'{name}.session'):
                self.email = input('Enter Your Email: ')
                self.password = input('Enter Your Password: ')

                result = self.execute(
                    service='login', method='post', data={
                        'email': self.email, 'password': self.password
                    }
                )
                print(result.json())
                if result.status_code != requests.codes.ok:
                    result_json = result.json()
                    raise Exception(result_json.get('message'))

                result = result.json()
                self.token = result.get('api_token')

                with open(f'{name}.session', 'w') as session_file:
                    json_rows = {
                        'api_token': self.token
                    }
                    session_file.write(json.dumps(json_rows))
            else:
                with open(f'{name}.session', 'r') as session_file:
                    result = eval(session_file.read())
                    self.token = result.get('api_token')

    @property
    def base_url(self) -> str:
        return f'https://api.iran.liara.ir/v{self.version}/'

    def execute(self, service: str, method: str, data: Optional[dict] = None) -> requests.Response:
        headers: dict = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fa;q=0.6',
            'Authorization': f'Bearer {self.token}',
            'Origin': 'https://console.liara.ir',
            'Referer': 'https://console.liara.ir/',
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            )
        }
        result = self.session.request(
            method=method, url=self.base_url + service, headers=headers, timeout=self.timeout, json=data
        )
        if result.json().get('error') == 'Unauthorized.':
            raise errors.Unauthorized('Unauthorized account or session!')

        return result

    def get_projects(self):
        '''
        Get details of all projects
        '''
        return self.execute(service='projects', method='get')

    def get_my_account(self):
        '''
        Get account information
        '''
        return self.execute(service='me', method='get')

    def off_service(self, service_name: str):
        '''
        Turn off a app
        '''
        params: dict = {
            'scale': '0'
        }
        return self.execute(
            service=f'projects/{service_name}/actions/scale', method='post', data=params
        )

    def on_service(self, service_name: str):
        '''
        Turn on a app
        '''
        params: dict = {
            'scale': '1'
        }
        return self.execute(
            service=f'projects/{service_name}/actions/scale', method='post', data=params
        )

    def restart_service(self, service_name: str):
        '''
        To restart a app
        '''
        return self.execute(service=f'projects/{service_name}/actions/restart', method='post')

    def delete_service(self, service_name: str):
        '''
        Delete a app
        '''
        return self.execute(service=f'projects/{service_name}/actions/restart', method='delete')

    def get_process(self, service_name: str):
        '''
        Get summary reports of app
        '''
        return self.execute(service=f'projects/{service_name}/metrics/summary', method='get')

    def get_logs(self, service_name : str, second_update: Optional[int] = None):
        '''
        Get logs of app
        '''
        params: dict = {
            'since': 1
        }
        if second_update != None:
            time.sleep(second_update)
            return self.execute(service=f'projects/{service_name}/logs', method='get', data=params)
        else:
            return self.execute(service=f'projects/{service_name}/logs', method='get', data=params)
