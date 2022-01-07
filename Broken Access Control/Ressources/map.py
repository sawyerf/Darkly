#!/usr/local/bin/python3
import requests
import re
import sys

def get(url):
	if '..' in url:
		return
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

get('http://192.168.56.104/.hidden/')
