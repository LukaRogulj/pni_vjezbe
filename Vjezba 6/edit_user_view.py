#!C:\Users\Luka\AppData\Local\Programs\Python\Python39\python.exe
import base
import os,cgi
import session
import user
from enum import Enum

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
		edit_id = params.getvalue("edit_id")
        
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    user_id = params.getvalue("edit_id")#hvata se iz url-a ali moglo se dodati i kroz hidden input
    username = params.getvalue("username")
    gender = params.getvalue("gender")
    role = params.getvalue("role")
    user.update_user(user_id, username, gender, role)
    print("Location: users.py")

class Genders(Enum):
    m : 1
    f : 2
    o : 3



print ()
base.start_html()
user_obj = user.get_user(edit_id)
curr_role = user.get_user_role(edit_id)
print ('<form method="POST">')
print ('Username: <input type="text" name="username" value="'+ user_obj[1] +'"><br>')
print ('Gender: <input type="text" name="curr_gender" value="'+ user_obj[3] +'"><br>')
print ('''Select gender: <select name="gender">
            <option value="M">
            Male</option>

            <option value="F">
            Femail</option>
            
            <option value="-">
            Other</option>
            </select><br>''')
# TODO provjerit zasto ne radi import enum
#print (f'''Select gender: <select name="gender">
 #           <option value={Genders.m.name}>
  #          {Genders.m.name}</option>
#
 #           <option value={Genders.f.name}>
  #          {Genders.f.name}</option>

   #         <option value={Genders.o.name}>
    #        {Genders.o.name}</option>
     #       </select><br>''')

print ('Current role: '+ curr_role + '<br>')
print ('''Select role: <select name="role">
            <option value=2>
            ADMIN</option>

            <option value=1>
            USER</option>
            </select><br>''')
print ('<br><input type="submit" value="Edit">')
print ('</form>')
base.finish_html()