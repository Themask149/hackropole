# Password Manager

Après s'être connecté via netcat, mon premier réflexe est de mettre un breakpoint sur le main et de le disassemble : 

```bash 
(gdb) disassemble main
Dump of assembler code for function main:
   [...]
   0x000000000000126b <+262>:   lea    0xd96(%rip),%rdi        # 0x2008
   0x0000000000001272 <+269>:   call   0x1030 <puts@plt>
   0x0000000000001277 <+274>:   mov    0x2dca(%rip),%rax        # 0x4048 <stdout@GLIBC_2.2.5>
   0x000000000000127e <+281>:   mov    %rax,%rdi
   0x0000000000001281 <+284>:   call   0x1050 <fflush@plt>
   0x0000000000001286 <+289>:   movl   $0x0,-0x4(%rbp)
   0x000000000000128d <+296>:   jmp    0x12b1 <main+332>
   0x000000000000128f <+298>:   mov    -0x4(%rbp),%eax
   0x0000000000001292 <+301>:   cltq
   0x0000000000001294 <+303>:   movzbl -0x460(%rbp,%rax,1),%eax
   0x000000000000129c <+311>:   xor    $0x2a,%eax
   0x000000000000129f <+314>:   mov    %eax,%edx
   0x00000000000012a1 <+316>:   mov    -0x4(%rbp),%eax
   0x00000000000012a4 <+319>:   cltq
   0x00000000000012a6 <+321>:   mov    %dl,-0x4b0(%rbp,%rax,1)
   0x00000000000012ad <+328>:   addl   $0x1,-0x4(%rbp)
   0x00000000000012b1 <+332>:   cmpl   $0x43,-0x4(%rbp)
   0x00000000000012b5 <+336>:   jle    0x128f <main+298>
   0x00000000000012b7 <+338>:   lea    -0x4b0(%rbp),%rax
   0x00000000000012be <+345>:   mov    $0x0,%esi
   0x00000000000012c3 <+350>:   mov    %rax,%rdi
   0x00000000000012c6 <+353>:   mov    $0x0,%eax
   0x00000000000012cb <+358>:   call   0x1060 <open@plt>
   0x00000000000012d0 <+363>:   mov    %eax,-0x8(%rbp)
   0x00000000000012d3 <+366>:   cmpl   $0x0,-0x8(%rbp)
   0x00000000000012d7 <+370>:   jns    0x12e5 <main+384>
   0x00000000000012d9 <+372>:   lea    0xd58(%rip),%rdi        # 0x2038
   0x00000000000012e0 <+379>:   call   0x1030 <puts@plt>
   0x00000000000012e5 <+384>:   lea    -0x410(%rbp),%rcx
   0x00000000000012ec <+391>:   mov    -0x8(%rbp),%eax
   0x00000000000012ef <+394>:   mov    $0x80,%edx
   0x00000000000012f4 <+399>:   mov    %rcx,%rsi
   0x00000000000012f7 <+402>:   mov    %eax,%edi
   0x00000000000012f9 <+404>:   call   0x1040 <read@plt>
[...]
```

On repère l'appel à la fonction open à main+358, ainsi cela me donne envie de voir les fichiers qui ont été ouvert à la fin du main 

Pour cela, je fais un break à main+429. Après j'obtiens le numéro du processus en faisant "info proc". Ensuite il n'a plus qu'à regarder les file descriptors associés à ce processus : 

```bash 
(gdb) info proc
process 42
cmdline = '/app/password-manager'
cwd = '/app'
exe = '/app/password-manager'
(gdb) c
Continuing.
Welcome to my super secure password manager!

Breakpoint 2, 0x0000555555555301 in main ()
(gdb) shell ls -l /proc/42/fd
total 0
lrwx------ 1 ctf ctf 64 Dec 27 17:47 0 -> socket:[381937]
lrwx------ 1 ctf ctf 64 Dec 27 17:47 1 -> socket:[381937]
l-wx------ 1 ctf ctf 64 Dec 27 17:47 2 -> pipe:[369723]
lrwx------ 1 ctf ctf 64 Dec 27 17:47 3 -> socket:[382220]
lrwx------ 1 ctf ctf 64 Dec 27 17:47 4 -> socket:[382221]
lr-x------ 1 ctf ctf 64 Dec 27 17:47 5 -> /app/5a3ee44c763d76bd0222eb8db9265c5a010592f24d4aa311b5a72c5f5d693b59.txt
(gdb) shell cat /app/5a3ee44c763d76bd0222eb8db9265c5a010592f24d4aa311b5a72c5f5d693b59.txt
```

On trouve un fichier intéressant qui contient le shell ! 