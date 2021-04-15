#!C:\Users\Luka\AppData\Local\Programs\Python\Python39\python.exe


import base
import cgi
import os
import authentication
import db
import password_utils


password_change_error = "Password Change Error!"
user = None

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    password = params.getvalue("password")
    password_repeat = params.getvalue("password_repeat")
    secret_question = params.getvalue("secret_question")
    secret_answer = params.getvalue("secret_answer")

    validation_error = False
    success = False

    user = db.get_user(username)

    if not user:
        password_change_error += "<br>User with username " + username + " does not exist!"
        validation_error = True

    elif not password_utils.verify_password(secret_answer, user[5]):
        password_change_error += "<br>Wrong secret answer!"
        validation_error = True

    if password != password_repeat:
        password_change_error += "<br>Passwords must match!"
        validation_error = True

    if validation_error == False:
        authentication.change_password(user[1], password)
        print('Location: login.py')

print("")
base.start_html()
print(''' 
    <form method="POST">
        username <input type="text" name="username" required /><br>
        secret question
        <select name="secret_question">
            <option value="What is your childhood friends name?">
            What is your childhood friends name?</option>
            
            <option value="What is your dogs name?">
            What is your dogs name?</option>

        </select><br>            
        secret answer <input type="text" name="secret_answer" required/><br>
        password <input type="password" name="password" required/><br>
        repeat password <input type="password" name="password_repeat" required/><br>
        <input type="submit" value="Change Password"/>
    </form>
''')
print("<a href=index.py>Home</a>")
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>" + password_change_error + "</div>")
base.finish_html()