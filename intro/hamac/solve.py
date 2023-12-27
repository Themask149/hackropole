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
        # password = "omgh4xx0r"
        
        key = SHA256.new(password).digest()
        hmac = HMAC.new(password, digestmod=SHA256)
        hmac.update(b"FCSC2022")
        
        if hmac.hexdigest() == h:
            print(b"Password found: " + password)
            cipher = AES.new(key, AES.MODE_CBC, iv=bytes.fromhex(iv))
            try:
                decrypted = cipher.decrypt(bytes.fromhex(c))
                print(f"Password found: {password.decode()}")
                print(f"Decrypted data: {decrypted}")
                break
            except ValueError:
                continue