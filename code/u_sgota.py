import requests
import re
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
print(filtered)
