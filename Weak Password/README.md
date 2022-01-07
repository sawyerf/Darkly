 Weak Password

- La DB s'appelle Member_Brute_Force on comprends donc qu'il faut bruteforce le mot de passe
- Je cree un script qui bruteforce avec les 100 passwords les plus utilise
```
$> python3 script.py
123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
696969
shadow
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```
- On voit que le mot de passe shadow retourne une page plus grande que les autres
- On entre donc les login admin shadow et on a le flag
```
The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```
