#!C:\Users\Luka\AppData\Local\Programs\Python\Python39\python.exe
import cgi
params = cgi.FieldStorage()
ime = params.getvalue("ime")
lozinka = params.getvalue("lozinka")
status = params.getvalue("status")
email = params.getvalue("email")
smjer =params.getvalue("smjer")
zavrsni = params.getvalue("zavrsni")
napomena= params.getvalue("napomena")
if(zavrsni is None):
    zavrsni="Ne"

print ('''
<!DOCTYPE html>
<html>
<body>

<h2>List:</h2>

<form >
    
''')
print("Ime:  ")
print(ime)
print("<br><br>")
print("Status:  ")
print(status)
print("<br><br>")
print("E-mail:  ")
print(email)
print("<br><br>")
print("Smjer:  ")
print(smjer)
print("<br><br>")
print("Zavrsni:  ")
print(zavrsni)
print("<br><br>")
print("Napomena:  ")
print(napomena)



print ('''<br><br>
    <a href="1.py">Na pocetak</a>

</body>
</html>''')


