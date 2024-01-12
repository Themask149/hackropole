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
        
