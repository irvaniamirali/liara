# Liara
Unofficial library for account management and services in [Liara](https://liara.ir) Cloud


# Install & Update
```bash
pip install -u liara-cloud
```


### Quik start
```python
from liara import Client

client = Client(name='my_account')

result = client.get_my_account()
print(result)
```
