#!C:\Users\Luka\AppData\Local\Programs\Python\Python39\python.exe
import base
import cgi, os
import authentication

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    password = params.getvalue("password")
    success = authentication.register(username, password)
    if success:
        print('Location: login.py')
print()
base.start_html()
print ('''<form method="POST">
username <input type="text" name="username" />
password <input type="password" name="password"/>
<input type="submit" value="Register"/>
</form>''')
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Registration Error</div>")
base.finish_html()