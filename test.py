import types
import requests
from log import Log

urlList = set()

# respose = html.json()
respose = ['int', 'str', 'NoneType', 'bool', 'float'];
for i, v in enumerate(respose):
    Log.info(i)


#'int', 'str', 'NoneType', 'bool', 'float'
