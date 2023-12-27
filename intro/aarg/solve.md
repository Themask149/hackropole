# AAARG

On utilise ghidra pour décompiler le main : 

```c
undefined8 FUN_00401190(int param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  char *local_10;
  
  uVar1 = 1;
  if (1 < param_1) {
    uVar2 = strtoul(*(char **)(param_2 + 8),&local_10,10);
    uVar1 = 1;
    if ((*local_10 == '\0') && (uVar1 = 2, uVar2 == (long)-param_1)) {
      uVar2 = 0;
      do {
        putc((int)(char)(&DAT_00402010)[uVar2],stdout);
        uVar2 = uVar2 + 4;
      } while (uVar2 < 0x116);
      putc(10,stdout);
      uVar1 = 0;
    }
  }
  return uVar1;
}
```

Ici param_1 est couramment appelé argc et param_2 est couramment appelé argv
Ce qu'on veut donc c'est que la valeur du premier argument soit égale à -argc. 

testons: 

````bash
./aaarg -2
FCSC{f9a38adace9dda3a9ae53e7aec180c5a73dbb7c364fe137fc6721d7997c54e8d}
```