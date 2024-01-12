# A l'ancienne 

Il s'agit d'une exfiltration DNS: https://www.nomios.fr/actualite/lexfiltration-dns/

J'ouvre le fichier cap avec wireshark. 
Regardonc une requête DNS pour bien comprendre : 


```
Frame 15: 267 bytes on wire (2136 bits), 267 bytes captured (2136 bits)
Ethernet II, Src: VMware_0a:0e:83 (00:0c:29:0a:0e:83), Dst: VMware_5c:45:67 (00:0c:29:5c:45:67)
Internet Protocol Version 4, Src: 172.16.76.135, Dst: 172.16.76.134
User Datagram Protocol, Src Port: 53592, Dst Port: 53
Domain Name System (query)
    Transaction ID: 0x9995
    Flags: 0x0120 Standard query
    Questions: 1
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 1
    Queries
        QFnIMv66emLOvPmDsJI5DzCmm51A4bs21J830TgJr1-.JVFWk/gDaehSEI3MhJZVf1bXjGjyA/*65vYi9qlYje-.G9WFcxagN*efkM8Cn4WqfOPmrV6kmrhN2x/RIER0Ou-.eBjlkaJMcmrN8pCjQELcse*IsUDWLmswqQhXJTRtQq-.cGFzc3dk: type A, class IN
    Additional records
        <Root>: type OPT
    [Response In: 16]

```
Dans Queries, on a justement la requête fait au domaine .CGFzc3dk (qui veut dire passwd en base64). 
On va donc récupérer toutes les requêtes qui sont envoyées au domaine .CGFzc3dk, puis retirer les points et autres caractères qui ne sont pas décodables en base64 et tout mettre dans un fichier.

```python
import json



with open("dump.json", "r") as f:
    data = json.load(f)

with open("extract","w") as f:
    for packet in data:
        dns_layer = packet["_source"]["layers"]["dns"]
        dns_query = list(dns_layer["Queries"].values())[0]["dns.qry.name"]
        secret_datas=dns_query.split('.')
        if secret_datas[-1]=="cGFzc3dk":
            for x in secret_datas[:-1]:
                f.write(x.replace("*","+").replace("-","").replace(".",""))
        

```

Une fois le fichier obtenu, on le decode avec b64: base64 -d extract > extract_clear

Puis: 
```bash
$file extract_clear
extract_clear: gzip compressed data, was "passwd", last modified: Thu Mar 17 12:45:11 2022, from Unix, original size modulo 2^32 2798
```

On utilise zcat pour le print, mais je ne trouve pas le file

