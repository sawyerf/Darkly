# Broken Authentification

On peut voir en inspectant les cookies un cookie nommé I_am_admin ayant pour valeur `68934a3e9455fa72420237eb05902327` qui est le md5 de false. 
On a donc juste à modifier le cookie par la valeur `b326b5062b2f0e69046810717534cb09` qui est le md5 de true afin de récupérer le flag.