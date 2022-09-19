# import urllib3
# import json
# url = 'http://noithatlucmo.local/test-json'

# http = urllib3.PoolManager()
# r = http.request('GET', url)
# data = json.loads(r.data)
# print(data)

import requests
url = 'http://noithatlucmo.local/test-json'
x = requests.get(url)

print(x.text)


