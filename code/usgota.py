import urequests
import re
import utime
import uos
import json
def update(url):
    r =urequests.request("GET",url,headers={"user-agent":"cj667113"})
    s=(r.json())
    filtered=s[0]["commit"]["author"]["date"]
    prefl=url
    prfl_filter= re.search('(path.*.py$)',prefl)
    prfl_filter= prfl_filter.group(0).replace('path=','')
    prfl_filter= prfl_filter.split(r'/')
    for x in prfl_filter:
        if re.search('.*.py',x):
            code_name=x
            version_name=code_name.replace('.py','_version.log')
        else:
            pass
    print(code_name)
    try:
        uos.stat(version_name)
        print('exists')
    except:
        f=open(version_name,"w+")
        f.write(code_name+"|"+filtered)
        f.close()
    d1 = open(version_name,'r')
    d1 = d1.readline()
    d1 = d1.split("|")
    d1 = (d1[1])
    d2 = (filtered)
    d1= d1.replace(":",",").replace("Z","").replace("-",",").replace("T",",")
    d2= d2.replace(":",",").replace("Z","").replace("-",",").replace("T",",")
    d1=d1.split(",")
    d2=d2.split(",")
    d1_collect=[]
    d2_collect=[]
    for x in d1:
        x = int(x)
        d1_collect.append(x)
    for x in d2:
        x = int(x)
        d2_collect.append(x)
    d1=d1_collect
    d2=d2_collect
    for i in range(2):
        d1.append(None)
        d2.append(None)
    utime.mktime(d1)
    utime.mktime(d2)
    print(d1)
    print(d2)
    if d1==d2:
        print(code_name+" is up to date")
    else:
        print("Updating Code:"+code_name)
        get_download_link = url
        get_download_link = get_download_link.replace(r'commits?path=','contents/')
        get_download_link =urequests.get(get_download_link)
        get_download_link=(get_download_link.json())
        download_link=(get_download_link["download_url"])
        nv=urequests.get(download_link)
        f=open(code_name,'w+')
        f.write(nv.content)
        f.close()
        f=open(version_name,"w+")
        f.write(code_name+"|"+filtered)
        f.close()
        print("Update Complete")
