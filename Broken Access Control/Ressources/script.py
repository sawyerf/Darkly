import requests
import re
import sys

def get(url):
	if '..' in url:
		return
	r = requests.get(url)
	urls = re.findall(r'href="(.+?)"', r.text)
	if 'README' in url:
		print(r.text)
	for iurl in urls:
		get(url + iurl)
	return

get('http://192.168.56.104/.hidden/')
