# Not so FAT

Tout d'abord regardons quel type de fichier nous avons : 

```bash
$ file not-so-fat.dd
not-so-fat.dd: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, reserved sectors 4, root entries 512, sectors 32768 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 32, sectors/track 32, heads 64, serial number 0x3be84c04, unlabeled, FAT (16 bit)
```

Il faut retrouver un fichier à l'intérieur de celui-ci, pour cela j'utilise foremost. 

```
$ foremost not-so-fat.dd
Processing: not-so-fat.dd
|foundat=flag.txtUT
*|
```

Il nous sort un zip contenant le fichier flag.txt. Cependant le zip possède un mot de passe ! 

C'est le moment de sortir notre ami John. 

```
$ zip2john 00000104.zip > myhashzip
ver 1.0 efh 5455 efh 7875 00000104.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=59, decmplen=47, crc=007E07DB ts=4EB7 cs=4eb7 type=0
$ john myhashzip
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 12 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
0g 0:00:00:00 DONE 1/3 (2023-12-19 11:58) 0g/s 202414p/s 202414c/s 202414C/s Txt000001041900..Tflag1900
Proceeding with wordlist:/opt/tools/john/run/password.lst
Enabling duplicate candidate password suppressor
password         (00000104.zip/flag.txt)
1g 0:00:00:00 DONE 2/3 (2023-12-19 11:58) 2.632g/s 139247p/s 139247c/s 139247C/s 123456..123qweas
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Le mot de passe est password, il ne suffit plus qu'à unzip et cat le flag! 