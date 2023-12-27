# Hamac

Voici ce que l'on nous donne dans le output.txt : 
{"iv": "ea425b2ea4bb67445abe967e3bd1b583", "c": "69771c85e2362a35eb0157497e9e2d17858bf11492e003c4aa8ce1b76d8d3a31ccc3412ec6e619e7996190d8693299fc3873e1e6a96bcc1fe67abdf5175c753c09128fd1eb2f2f15bd07b12c5bfc2933", "h": "951bd9d2caae0d9e9a5665b4fc112809aac9f5f9ecbcfc5ad8e23cb1d020201d"}

L'énoncé nous parle de rockyou, donc mon petit doigt me dit qu'il faudra bruteforce le HMAC. 

Pour cela, j'avais élaboré un petit script en python : 

```python
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

iv=""
c=""
h=""

with open("output.txt","r") as f:
    jsonline=f.readline()
    jsonline=json.loads(jsonline)
    iv=jsonline["iv"]
    c=jsonline["c"]
    h=jsonline["h"]
    

with open("/opt/rockyou.txt", "rb") as file:
    i=0
    for password in file:
        
        hmac = HMAC.new(password, digestmod=SHA256)
        hmac.update(b"FCSC2022")
        
        if hmac.hexdigest() == h:
            key = SHA256.new(password).digest()
            print(b"Password found: " + password)
            cipher = AES.new(key, AES.MODE_CBC, iv=bytes.fromhex(iv))
            try:
                decrypted = cipher.decrypt(bytes.fromhex(c))
                print(f"Password found: {password.decode()}")
                print(f"Decrypted data: {decrypted}")
                break
            except ValueError:
                continue
```

Malheureusement, ce script est beaucoup trop lent pour bruteforce le hmac. Il faudra trouver une autre méthode ! Heureusement d'autres outils comme john existe pour aller plus vite, en effet il propose le format: HMAC-SHA256 ! 

Mettez le hash dans un fichier hash.txt : FCSC2022#951bd9d2caae0d9e9a5665b4fc112809aac9f5f9ecbcfc5ad8e23cb1d020201d

et lancez john : `john --wordlist=/opt/rockyou.txt --format=HMAC-SHA256 hash.txt`

Après quelques instants, on trouve que le password est omgh4xx0r. 

On peut donc décrypter le flag ! 

FCSC{5bb0780f8af31f69b4eccf18870f493628f135045add3036f35a4e3a423976d6}