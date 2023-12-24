# 2tp

Un article cool à lire pour continuer la réflexion sur AES-GCM: https://soatok.blog/2020/05/13/why-aes-gcm-sucks/

Voici le schéma pour comprendre AES en mode GCM tiré de Wikipédia
<p><a href="https://commons.wikimedia.org/wiki/File:GCM(1).svg#/media/Fichier:GCM(1).svg"><img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/GCM%281%29.svg" alt="GCM(1).svg" height="419" width="1482"></a><br>

On s'intéresse qu'à la partie haute du schéma où on obtient le ciphertext, on n'a pas besoin de la partie tag. 

Nous avons Ciphertext i = Plaintext i xor E_K(Counter i) pour i un entier. 

De plus, le service nous donne la possibilité de chiffrer nos propres textes. En testant avec le début supposé du flag, j'obtiens : 

```bash
Welcome to our state-of-the-art encryption service!
We use PBKDF2 and AES-GCM!
As an example, here is the encrypted flag: 7b656d3993152e8f04f8273ca1509e27a3e39249cf4784e23b81d5f2524fee75f6b28a6a07a128e4880e770bc70b32bd7d5f37bb5eba76d38edb8d1964733b
Now, enter your text: ECSC{
Here is your ciphertext: 7b656d3993d956d6c1d7b2348bbf8ebc224d70d869
```

On remarque que les 5 premiers bytes sont les mêmes, ce qui m'indique que l'IV/nonce est le même à chaque fois. 

Or Ciphertext i = Plaintext i xor E_K(Counter i)
et Flag_encrypted i = Flag i xor E_k(Counter i)

Donc Ciphertext i xor Flag_encrypted i xor Plaintext i = Plaintext i xor E_K(Counter i) xor Flag i xor E_k(Counter i) xor Plaintext i = Flag i ! 

Testons cela directement ! 

```python
from pwn import remote

def xor(s1, s2):
    if(len(s1) == 1 and len(s1) == 1):
        return bytes([ord(s1) ^ ord(s2)])
    else:
        return bytes(x ^ y for x, y in zip(s1, s2))

def main():
    payload = b'A' * 50
    conn = remote('172.25.106.194', 4000)
    conn.recvline()
    conn.recvline()
    
    flag_enc = conn.recvline().decode().split(": ")[1][:-1].strip()
    flag_enc = bytes.fromhex(flag_enc)
    conn.sendlineafter(b"Now, enter your text: ", payload)
    ciphertext = conn.recvline().decode().split(": ")[1][:-1].strip()
    ciphertext = bytes.fromhex(ciphertext)
    print(ciphertext,flag_enc)
    flag = xor(xor(flag_enc, ciphertext), payload)
    print(flag)
    conn.close()

if __name__ == '__main__':
    main()

```

Et le flag nous est donné en sortie ! 

