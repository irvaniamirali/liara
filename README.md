## Liara
> Unofficial library for account management and services in [Liara](https://liara.ir) Cloud

### Quik start
```python
from liara import Client

client = Client(name="my_account")

result = client.get_my_account()
print(result.fullname)
```

### Another Login Example
```python
from liara import Client

api_token = "API_TOKEN"

client = Client(api_token=api_token)

result = client.get_my_account()
print(result.fullname)
```

### Contribution
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### Install & Update
```bash
pip install -U liara-cloud
```
