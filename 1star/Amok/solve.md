# Amok

Avec dcode.fr, le ciphertext est probable un Pollux code. Pour faire simple chaque lettre ou chiffre représente soit un point, soit un tiret ou soit un espace, et ensuite il faut traduire du morse le message secret.

On pourrait décider de faire un bruteforce sur toutes les combinaisons possibles. Chaque caractère a 3 possibilités donc cela nous donne 3^36 possibilités ce qui est quand même énorme, il faut trouver des astuces pour réduire cela. 
On remarque que le message est quand même très très long et on sait que le message doit être lisible

![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/260px-International_Morse_Code.svg.png)

Ici, on voit que la distance maximale entre 2 espaces est de 5, ce qui nous donne une info précieuse. Par exemple cette ligne:

3NK4Z 7X30H 631N7 U9KWN VE3BY NBCY5 13VX7

On sait que [3NK4Z7] ne représentent pas le même caractère (point, tiret ou espace,  et il y a toujours un espace). Pareil pour [NK4Z7X], [K4Z7X3] etc...

Pareil il n'y a jamais 3 espaces d'affilés, donc ma première idée est la suivante. On construit tous les ensembles de 3 lettres ou chiffres, on lit le ciphertext, et on enlève tous les suites de 3 lettres ou chiffres qui apparaissent dans le ciphertext. On aura à la fin la liste des ensembles possibles pour le caractère espace

