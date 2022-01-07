IP="192.168.56.104"
wget http://${IP}/.hidden/

for i in $(cat index.html | grep '<a' | cut -d'"' -f 2); do
	curl http://${IP}/.hidden/$i 2>&- > folder_list
	for folder in $(cat folder_list | grep '<a' | cut -d'"' -f 2); do
		echo http://${IP}/.hidden/$i/$folder/README
		curl http://${IP}/.hidden/$i/$folder/README 2>&- | grep flag
	done
done
