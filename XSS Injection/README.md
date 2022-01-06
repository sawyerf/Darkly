# XSS Injection

- Dans ce formulaire on peut y mettre des commentaire visible par tout les user
- On comprends donc qu'il faut y mettre un script js pour qu'il soit interpreter par les autres user
- Les balise <script> sont supprimer mais en y mettant des majuscules cela fonctionne
```html
<ScrIpT>alert("lol");</ScrIpT>
```
- et voici le flag
The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
