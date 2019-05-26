import requests
import re
import datetime
r =requests.get('https://api.github.com/repos/cj667113/simple_github_ota_updater/commits?path=code/u_sgota.py')
collect=[]
for x in r:
    y=(re.search('"date"(.*)}',x))
    try:
        collect.append(y.group())
    except:
        pass
        
filtered=collect[0]
filtered=(re.sub('"','',filtered))
filtered=(re.sub('}','',filtered))
filtered=(re.sub('date:','',filtered))
d1 = datetime.datetime.now().date()
d2 = datetime.datetime.strptime(filtered,"%Y-%m-%dT%H:%M:%SZ").date()
print(d1)
print(d2)

if d1>d2:
    print("true")
else:
    print("false")
