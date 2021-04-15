#!C:\Users\Luka\AppData\Local\Programs\Python\Python39\python.exe
import base
import cgi
import session
import user

params = cgi.FieldStorage()

data = session.get_session_data()
if data is None: # tko nema sessiju nije logiran. - idi na login
    print ("Location: login.py")
else:
	user_id = data.get("user_id", None)
	user_role = user.get_user_role(user_id)
	if user_role != "ADMIN":
		print ("Location: index.py")
	else:
		delete_id = params.getvalue("delete_id")
		if delete_id:
			user.delete_user(delete_id)
print ()
base.start_html()
print ("<h1>USERS:</h1>")
users = user.get_all_users()
print ("<table border=1>")
for user in users:
	print ("<tr>")
	print ("<td>" + user[1] + "</td>")
	print('<td><a href="edit_user_view.py?edit_id='+ str(user[0]) +'">edit</a></td>')
	print('<td><a href="users.py?delete_id='+ str(user[0]) +'">delete</a></td>')
	print ("</tr>")
print ('<tr><td><a href="register.py">add user</a></td></tr>')
print ("</table>")
base.finish_html()
