# Tarte Tatin 

Comme il faut extraire le flag du binaire, je vais suivre la technique du fainéant. Je vais forcer pour suivre les bonnes branches conditionnelles pour récupérer le flag à la fin, sans comprendre comment le flag a été transformé. 

Effectivement, le flag a été transformé car on ne le retrouve pas en utilisant simplement la fonctions strings, de plus on retrouve la fonction transform lorsqu'on "disassemble" le main 

```assembly
000000000000077a <transform>:
 77a:   55                      push   %rbp
 77b:   48 89 e5                mov    %rsp,%rbp
 77e:   48 89 7d f8             mov    %rdi,-0x8(%rbp)
 782:   48 8b 45 f8             mov    -0x8(%rbp),%rax
 786:   48 8d 50 01             lea    0x1(%rax),%rdx
 78a:   48 89 55 f8             mov    %rdx,-0x8(%rbp)
 78e:   0f b6 10                movzbl (%rax),%edx
 791:   83 c2 01                add    $0x1,%edx
 794:   88 10                   mov    %dl,(%rax)
 796:   48 8b 45 f8             mov    -0x8(%rbp),%rax
 79a:   0f b6 00                movzbl (%rax),%eax
 79d:   84 c0                   test   %al,%al
 79f:   75 e1                   jne    782 <transform+0x8>
 7a1:   90                      nop
 7a2:   5d                      pop    %rbp
 7a3:   c3                      retq

00000000000007a4 <main>:
 7a4:   55                      push   %rbp
 7a5:   48 89 e5                mov    %rsp,%rbp
 7a8:   48 83 ec 30             sub    $0x30,%rsp
 7ac:   64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
 7b3:   00 00
 7b5:   48 89 45 f8             mov    %rax,-0x8(%rbp)
 7b9:   31 c0                   xor    %eax,%eax
 7bb:   48 8b 15 ce 08 20 00    mov    0x2008ce(%rip),%rdx        # 201090 <stdin@@GLIBC_2.2.5>
 7c2:   48 8d 45 d0             lea    -0x30(%rbp),%rax
 7c6:   be 20 00 00 00          mov    $0x20,%esi
 7cb:   48 89 c7                mov    %rax,%rdi
 7ce:   e8 7d fe ff ff          callq  650 <fgets@plt>
 7d3:   48 8d 45 d0             lea    -0x30(%rbp),%rax
 7d7:   48 89 c7                mov    %rax,%rdi
 7da:   e8 9b ff ff ff          callq  77a <transform>
 7df:   48 8d 45 d0             lea    -0x30(%rbp),%rax
 7e3:   ba 10 00 00 00          mov    $0x10,%edx
 7e8:   48 8d 35 91 08 20 00    lea    0x200891(%rip),%rsi        # 201080 <pass_enc>
 7ef:   48 89 c7                mov    %rax,%rdi
 7f2:   e8 49 fe ff ff          callq  640 <memcmp@plt>
 7f7:   85 c0                   test   %eax,%eax
 7f9:   75 1f                   jne    81a <main+0x76>
 7fb:   48 8d 3d 1e 08 20 00    lea    0x20081e(%rip),%rdi        # 201020 <flag_enc>
 802:   e8 73 ff ff ff          callq  77a <transform>
 807:   48 8d 3d 12 08 20 00    lea    0x200812(%rip),%rdi        # 201020 <flag_enc>
 80e:   e8 0d fe ff ff          callq  620 <puts@plt>
 813:   b8 01 00 00 00          mov    $0x1,%eax
 818:   eb 05                   jmp    81f <main+0x7b>
 81a:   b8 00 00 00 00          mov    $0x0,%eax
 81f:   48 8b 4d f8             mov    -0x8(%rbp),%rcx
 823:   64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
 82a:   00 00
 82c:   74 05                   je     833 <main+0x8f>
 82e:   e8 fd fd ff ff          callq  630 <__stack_chk_fail@plt>
 833:   c9                      leaveq
 834:   c3                      retq
 835:   66 2e 0f 1f 84 00 00    nopw   %cs:0x0(%rax,%rax,1)
 83c:   00 00 00
 83f:   90                      nop
```


Une ligne intéressante se trouve en 7f7, juste après le memcopy et juste avant le saut pour la condition. Si eax se trouve à 0 au moment de cette ligne, on rentrera dans la branche avec le puts qui nous affichera certainement le flag. 

J'ouvre gdb et je mets un breakpoint à cette ligne. Après avoir lancé le programme et mis une entrée random, je fais : set $eax=0. 

Après la commande continue, le flag nous est renvoyé ! 