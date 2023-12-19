from Crypto.Cipher import AES
from Crypto.Util import Counter

key = bytes.fromhex("00112233445566778899aabbccddeeff")

with open("flag.jpg.enc", "rb") as f:
    enc = f.read()
    counter = Counter.new(nbits=128, initial_value=0)
    aes = AES.new(key, AES.MODE_CTR,counter=counter)
    flag = aes.decrypt(enc)
    with open("flag.jpg", "wb") as f:
        f.write(flag)
    