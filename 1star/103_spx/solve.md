# 103_sp

Tout d'abord, on "mount" la clé USB de ce fan de moto :  `sudo mount -r USB_a_analyser /media`

```bash
$ ls -la
total 101
drwxrwxrwx  1 root root  4096 Jul  6  2019  .
drwxr-xr-x 20 root root  4096 Dec 22 21:52  ..
drwxrwxrwx  1 root root     0 Jul  6  2019  .Trash-1000
-rwxrwxrwx  1 root root 68873 Jul  6  2019 'Peugeot 103 SPX : tous les modèles de 1987 à 2003 | Actualités de la mobylette par Mobylette Mag.html'
drwrwxrwx  1 root root  8192 Jul  6  2019 'Peugeot 103 SPX : tous les modèles de 1987 à 2003 | Actualités de la mobylette par Mobylette Mag_files'
-rwxrwxrwx  1 root root 15041 Jul  6  2019  Peugeot103SPXFILI.jpg
-rwxrwxrwx  1 root root   577 Jul  6  2019  message.txt

$ cat message.txt
Si un jour je relis ce message, le mot de passe utilisé pour chiffrer mon plus grand secret était "vgrohhfyek0wkfi5fv13anexapy3sso6" et j'avais utilisé openssl.
En revanche, j'ai effacé par erreur le fichier contenant mon plus grand secret (voir s'il existe des techniques de la mort pour le retrouver mon fichier secret.xz sha256(0fb08681c2f8db4d3c127c4c721018416cc9f9b369d5f5f9cf420b89ee5dfe4e) de 136 octets) et de toute façon, impossible de me rappeler de l'algo utilisé -_- (donc si je le retrouve... il faudra aussi retrouver l'algo pour utiliser ce mot de passe).
```

On retrouve le fichier secret.xz dans le dossier .Trash-1000

Par contre, on ne connait pas l'algorithme de chiffrement qui va nous permettre de déchiffre. Je propose donc de bruteforcer. En faisant openssl help, on a une liste d'algos qui est proposée, je vais donc l'utiliser pour bruteforcer les algos avec ce script : 

```bash 

#!/bin/bash

ENCRYPTED_FILE="secret"
PASSWORD="vgrohhfyek0wkfi5fv13anexapy3sso6"
DECIPHERS=("aes-128-cbc" "aes-128-ecb" "aes-192-cbc" "aes-192-ecb" "aes-256-cbc" "aes-256-ecb" "aria-128-cbc" "aria-128-cfb" "aria-128-cfb1" "aria-128-cfb8" "aria-128-ctr" "aria-128-ecb" "aria-128-ofb" "aria-192-cbc" "aria-192-cfb" "aria-192-cfb1" "aria-192-cfb8" "aria-192-ctr" "aria-192-ecb" "aria-192-ofb" "aria-256-cbc" "aria-256-cfb" "aria-256-cfb1" "aria-256-cfb8" "aria-256-ctr" "aria-256-ecb" "aria-256-ofb" "base64" "bf" "bf-cbc" "bf-cfb" "bf-ecb" "bf-ofb" "camellia-128-cbc" "camellia-128-ecb" "camellia-192-cbc" "camellia-192-ecb" "camellia-256-cbc" "camellia-256-ecb" "cast" "cast-cbc" "cast5-cbc" "cast5-cfb" "cast5-ecb" "cast5-ofb" "des" "des-cbc" "des-cfb" "des-ecb" "des-ede" "des-ede-cbc" "des-ede-cfb" "des-ede-ofb" "des-ede3" "des-ede3-cbc" "des-ede3-cfb" "des-ede3-ofb" "des-ofb" "des3" "desx" "rc2" "rc2-40-cbc" "rc2-64-cbc" "rc2-cbc" "rc2-cfb" "rc2-ecb" "rc2-ofb" "rc4" "rc4-40" "seed" "seed-cbc" "seed-cfb" "seed-ecb" "seed-ofb" "sm4-cbc" "sm4-cfb" "sm4-ctr" "sm4-ecb" "sm4-ofb"
)

for cipher in "${DECIPHERS[@]}"; do
    echo "Trying $cipher..."
    openssl enc -d -$cipher -in "$ENCRYPTED_FILE" -out "decrypted_file" -pass pass:"$PASSWORD" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "Decryption successful with cipher: $cipher"
        exit 0
    fi
done

echo "Failed to decrypt file with provided ciphers."
```

Voici le résultat : 

```
 ./solve.sh
Trying aes-128-cbc...
Trying aes-128-ecb...
Trying aes-192-cbc...
Trying aes-192-ecb...
Decryption successful with cipher: aes-192-ecb
```

Et bam ! On a le flag dans le fichier decrypted_file ! 
