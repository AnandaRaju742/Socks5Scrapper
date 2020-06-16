import re
import requests
from bs4 import BeautifulSoup
r=requests.get("http://spys.one/en/socks-proxy-list/")
if r.status_code == 200:
    print('Site Working')
    #print(r.text)
    soup=BeautifulSoup(r.text,'html.parser')
    table=soup.find_all(name='tr',class_=re.compile(r'^spy1x$|^spy1xx$'))
    ip_addrs=[]
    ports=[]
    variables=soup.find('script',type="text/javascript").contents[0]
    exec(variables)
    #print(variables)
    for row in table:
        ipdata=row.find(name='font',class_='spy14')
        if ipdata == None:
            continue
        portdata=ipdata.find(name='script',type="text/javascript").contents
        ext_port=portdata[0][43:-1]
        #print(ext_port)
        #ext_port=ext_port.replace('+','print').replace(')',');')
        exec('port=int('+ext_port.replace('+','str',1).replace('+',"+''+str")+')')
        if port == None:
            continue
        #print(port)
        #print(ipdata.text)
        ports.append(port)
        ip_addrs.append(ipdata.text)
    for x,y in zip(ip_addrs,ports):
        print(str(x)+':'+str(y))
else:
    print('Site not working')
