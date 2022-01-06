# Broken Access Control
- http://192.168.56.104/robots.txt
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

La page http://192.168.56.104/.hidden est uh dossier contenant plein de dossiers au nom aléatoire et un README et chacun des dossiers a la même structure, on va donc aller inspecter tous les README a la recherche du flag grace au script `./Ressources/map.sh`