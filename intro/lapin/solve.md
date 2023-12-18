# La Pin 

Tout d'abord, regardons ce que fait le fichier lapin.py:

```python
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes

while True:
	pin = int(input(">>> PIN code (4 digits): "))
	if 0 < pin < 9999:
		break

flag = open("flag.txt", "rb").read()
k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1) 
aes = AES.new(k, AES.MODE_GCM)
c, tag = aes.encrypt_and_digest(flag)
enc = aes.nonce + c + tag
print(enc.hex())
```

Il prend un pin à 4 chiffres pour construire une clé. Cette clé sert à chiffrer flag.txt avec AES en mode Galois Counter Mode. Pas besoin de connaître ce mode dans les moindres détails, on peut essayer de bruteforcer la clé car il n'y a que 10000 possibilités. 

N'oublions pas d'extraire correctement le nonce, le cipher text et le tag du fichier.txt et c'est parti ! 

```python
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes

with open("output.txt", "rb") as f:
    hex_output= bytes.fromhex(f.readline().decode("utf-8")) #Attention à bien convertir notre output en bytes ! 
    nonce = hex_output[:16] # 16 bytes de nonce
    c= hex_output[16:-16]
    tag = hex_output[-16:] # 16 bytes de tag
    for i in range(1,10000):
        print("Pin: ",i)
        pin = i
        k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
        aes = AES.new(k, AES.MODE_GCM, nonce=nonce) # N'oublions pas le nonce ici ! 
        flag = aes.decrypt(c)
        if b"FCSC" in flag:
            print(flag)
            break
```

Comme on sait que le flag contient toujours FCSC, on s'arrête lorsqu'il est présent dans un de nos déchiffrements. Le programme s'arrête au PIN 6273 et nous donne le flag !

