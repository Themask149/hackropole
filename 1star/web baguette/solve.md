# Web Baguette 

Le challenge est très simple ! Première en regardant le code source de la page, nous voyons : 

```html
<!-- 
  Changelog :
    - Site web v0
    - /api/image : CDN interne d'images
    - /api/debug
  TODO :
    - VPN
-->
```

Sur /api/image, nous avons : Paramètre manquant
Sur /api/debug, on a quelque chose de plus intéressant:

On a des infos de debug sur l'application qui est une application Flask. Pour mieux voir les choses importantes, j'ai utilisé ce site pour voir clairement le json renvoyé: https://jsonformatter.org/json-viewer

On a une ligne intéressante : 

__file__	:	/app/baguettevpn_server_app_v0.py

Et le fichier contient les 2 flags des 2 challenges