# HTTP Header

- Dans la source de cette page il y a des commentaires qui donne des informations sur des headers a set dans la requete HTTP
```
Let's use this browser : "ft_bornToSec". It will help you a lot.
```
- Ce commentaire nous demande de set l'User-Agent qui identifie normalement le navigateur à `ft_bornToSec`

```
You must cumming from : "https://www.nsa.gov/" to go to the next step
```
- Ce commentaire nous demande de faire croire que l'on viens du site de la nasa la variable d'header qui habituellement fait ca est `Referer`
```
Referer: https://www.nsa.gov/
```

- En y mettant ce deux variables d'headers on obtien le flag
```
Referer: https://www.nsa.gov/
User-Agent: ft_bornToSec
```

```
The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```