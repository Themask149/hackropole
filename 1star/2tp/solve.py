#!/usr/bin/env python3

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