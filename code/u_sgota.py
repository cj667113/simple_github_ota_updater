import requests
import re
import datetime
import os
import json
def sgota(url):
    r =requests.get(url)
    s=(r.json())
    filtered=s[0]["commit"]["author"]["date"]
    prefl=url
    prfl_filter= re.search('(path.*.py$)',prefl)
    prfl_filter= re.sub('path=','',prfl_filter.group())
    prfl_filter= prfl_filter.split(r'/')
    for x in prfl_filter:
        if re.search('.*.py',x):
            code_name=x
            version_name=re.sub('.py','_version.log',code_name)
        else:
            pass
    print(code_name)
    file_location = os.path.isfile(version_name)
    if file_location:
        print('exists')
    else:
        f=open(version_name,"w+")
        f.write(code_name+"|"+filtered)
        f.close()
    d1 = open(version_name,'r')
    d1 = d1.readline()
    d1 = d1.split("|")
    d1 = datetime.datetime.strptime(d1[1],"%Y-%m-%dT%H:%M:%SZ")
    d2 = datetime.datetime.strptime(filtered,"%Y-%m-%dT%H:%M:%SZ")
    print(d1)
    print(d2)
    if d1==d2:
        print(code_name+" is up to date")
    else:
        print("Updating Code:"+code_name)
        get_download_link = url
        get_download_link = get_download_link.replace(r'commits?path=','contents/')
        get_download_link =requests.get(get_download_link)
        get_download_link=(get_download_link.json())
        download_link=(get_download_link["download_url"])
        nv=requests.get(download_link)
        f=open(code_name,'w+')
        f.write(nv.content)
        f.close()
        f=open(version_name,"w+")
        f.write(code_name+"|"+filtered)
        f.close()
        print("Update Complete")
sgota('https://api.github.com/repos/cj667113/simple_github_ota_updater/commits?path=code/u_sgota.py')
