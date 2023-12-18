from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.number import long_to_bytes

with open("output.txt", "rb") as f:
    hex_output= bytes.fromhex(f.readline().decode("utf-8"))
    nonce = hex_output[:16]
    c= hex_output[16:-16]
    tag = hex_output[-16:]
    for i in range(1,10000):
        print("Pin: ",i)
        pin = i
        k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
        aes = AES.new(k, AES.MODE_GCM, nonce=nonce)
        flag = aes.decrypt(c)
        if b"FCSC" in flag:
            print(flag)
            break

    