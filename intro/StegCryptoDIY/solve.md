# StegCryptoDIY

On a une image de référence et celle du challenge. Ma première idée était de faire un xor des 2 images mais cela n'a pas été concluant. 

Comme il s'agit d'un challenge, j'ai décidé de continuer sur des outils simples: 

```bash
$ strings leHACK19_chall.png | awk '{print length, $0}' | sort | head
1093 @duMBTiA9IDExNzU1MDY4OTQ0MTQyOTY5NDk4NzQzMjQ1OTg0NzYxMTgxMzI1NjA1MzA0NjI1Mjg2OTU4NzIxMzkxNzY2MDkxMjgzMTMyMzk4NDM3NjQ1MDM4MzQ5Nzc1ODk4OTIzNDY1MzMxMjYwMzA4MDY0NjExMTY3OTI2MTg3Mzk5Mzg0NzIzMzYwOTQxODgzNzMyMTc0OTAxNjY2ODAzICxnMSA9IDM4MDg4MTk1MDU1NjQ5OTk1NDUyNTI2MjM2MzExOTI1MDMyMTIxODY1OTgwODg1NTUzNDM3MzgxMTExNjUzODI2MjM0MjE3MjAxMTk4Mzc1NDQ2NTgxNzM4MjI0NjE4MzQwNzYzNDc3OTUxNTkzNjY1OTMxNzc2NjkwNTg3MDUwODcyNjY4OTg0NDQ4MTg5MjY2Njg1ODQ1MTksIGcyID0gODcyMTc4NzQwMDMyNzc4Mzc0ODAxNDg0OTAzNzYyNjAzOTM5NzgwNzYxMjM3MjgwNDAxNjY0MzY1MzA0NzU3NTk3NjAwOTgyNzAwMzQ0Nzc3ODg2MTI2MjAzNjc1MjMyNjgyNzYxMzA3ODM0NjIyNTE5MjU4MTcwODI0MDgyMDMyNTg2NzY1ODc0MjA3ODY5NDQ0NTY3Nzg3NyBJIHVzZSB0aGlzIGZ1bmN0b25zIGZvciBlbmNpcGhlcmluZyBvdXIgc2tleSA6IGVuY2lwaGVyKGludC5mcm9tX2J5dGVzKHNrZXksJ2JpZycpLGcxLGcyLE4pIHdpdGggZGVmIGVuY2lwaGVyKG0sZzEsZzIsTik6IHMxPXJhbmRvbS5yYW5kcmFuZ2UoMioqMTI3LDIqKjEyOCkgczI9cmFuZG9tLnJhbmRyYW5nZSgyKioxMjcsMioqMTI4KSByZXR1cm4gKG0qcG93KGcxLHMxLE4pKSVOLCAobSpwb3coZzIsczIsTikpJU4gYW5kIGhlcmUgaXMgYSBmbGFnOiBsZWhhY2syMDE5e2FlZjk1NTZhNTc1Y2M5ZGU4ZmM5NjA5YmQwMzRkNjNmZTBhMDE0NzBlYjQwMTM3ODI1M2Y3MjNiYmM1Y2MxNmN9
10 { )Ow%)kC\
10 uei|JK|z3y
11 $rUGNBV_Al.
11 :gf/;Xm$fx.
12 {.tO4b**;/""
4       +\#\"
4       ,/\"
4       {&
4 !=    *

$ strings leHACK19_ref.png | awk '{print length, $0}' | sort | head
10 hd=$z.,} c
10 J6C-8ak7Y?
12 tEXtSoftware
17 Adobe ImageReadyq
4       /'}
4  ,    |
4 ".~`
4 '-+]
4 '}\~
4 +/"(
```

On a une énorme string suspicieuse à l'intérieur de l'image du challenge mais pas celle de référence. 
On va demander à notre ami dcode ce qu'il en pense. Il nous confirme que c'est bien du base64 et en décodant, nous avons le flag ! 