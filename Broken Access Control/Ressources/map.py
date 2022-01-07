#!/usr/local/bin/python3
import requests
import re
import sys

def get(url, f):
	if '..' in url:
		return
	f.write(url + '\n')
	r = requests.get(url)
	urls = re.findall(r'href="(.+?)"', r.text)
	if 'README' in url:
		flags = re.findall(r'([A-Fa-f0-9]{10,})', r.text)
		if flags != []:
			print(flags)
			print(url)
		if 'flag'.casefold() in r.text.casefold():
			print(r.text)
		
	for iurl in urls:
		get(url + iurl, f)
	return

f = open('log.txt', 'w')
get('http://192.168.56.102/.hidden/', f)
f.close()
