import os
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor

output = open("output.txt", "r").read()
output = bytes.fromhex(output)
print(len(output))
#On sait que le flag commence par FCSC
#ça tombe bien, la clé est un string de longueur 4 répétée x fois
key = strxor(b"FCSC", output[:4])
print(strxor(output, (key*20)[:len(output)]).decode("utf-8"))
