# Header

En regardant le code source qui est donné dans un des endpoints du site, on peut voir cette partie intéressante


```javascript
[...]
app.get('/', async (req, res) => {
    var verif = req.header("X-FCSC-2022");
    if (verif == "Can I get a flag, please?") {
        var flag = fs.readFileSync("flag.txt");
        res.status(200);
        res.render("pages/index", {
            type: "success",
            msg: "Here it is: " + flag,
        });
        return res.end();
    } else {
        res.status(200);
        res.render("pages/index", {
            type: "warning",
            msg: "No flag for you. Want a meme instead?",
        });
        return res.end();
    }
});

[...]

```

Avec Burp, on va ajouter manuellement un header qui correspond exactement à la condition du code ci-dessus. 
Il suffit de rajouter "X-FCSC-2022: Can I get a flag, please?" dans les headers avant d'envoyer la requête pour obtenir le flag. 

FCSC{9ec57a4a72617c4812002726750749dd193d5fbbfeef54a27a9b536f00d89dfb}