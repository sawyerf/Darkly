# Leak Password

- http://192.168.56.104/robots.txt
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

- http://192.168.56.104/whatever/
```
root:8621ffdbc5698829397d97767ac13db3
```

- Le mot de passe de root correspond au md5 de dragon
- On va donc aller se log sur la page d'administration en utilisant `root:dragon` et récupérer le flag.