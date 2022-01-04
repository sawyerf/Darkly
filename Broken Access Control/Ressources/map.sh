wget http://192.168.56.102/.hidden/

for i in $(cat index.html | grep '<a' | cut -d'"' -f 2); do
	curl http://192.168.56.102/.hidden/$i 2>&- > folder_list
	for folder in $(cat folder_list | grep '<a' | cut -d'"' -f 2); do
		curl http://192.168.56.102/.hidden/$i/$folder/README 2>&- | grep flag
	done
done
