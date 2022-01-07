# LFI

- On voit que la variable page de `index.php` prend en paramètre une page à afficher.
- On essaye donc d'en sortir et d'y afficher un fichier exterieur au serveur web.
- On va donc passer en paramêtre `../etc/passwd` et l'on va remonter jusqu'à obtenir le flag.