#!C:\Users\Luka\AppData\Local\Programs\Python\Python39\python.exe


import cgi, os, sys, cgitb, base
import session



request_type = os.environ.get('REQUEST_METHOD', '')
if not os.path.isdir('../../htdocs/images'): #inace ce batiti gresku svaki put kad se post-a
    os.mkdir('../../htdocs/images')
 
images = os.listdir('../../htdocs/images')

form = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print ("Location: login.py")
    
print ("Content-type:text/html")
print ("")
base.start_html()
if (request_type == "POST"):
    #print(file_item)
    file_item = form["avatar"]
    if (file_item.filename):
        print('ime file-a ' + file_item.filename)
        print("<br>")
        #print(file_item.file)
    else:
        print ("<div>GRESKA!!</div>")

    if file_item.filename:
        fn = '../../htdocs/images/'
        fn += os.path.basename(file_item.filename)
        

        open(fn, 'wb').write(file_item.file.read(250000))
        message = 'The file "' + fn + '" was uploaded successfully'
    else:
        message = "No file was uploaded"
print (request_type)
print('<form enctype="multipart/form-data" method="POST">')
print ('<input type="file"  name="avatar" accept="image/png, image/jpeg">')
print('<input type="submit" value="upload" onClick="location.href=location.href">')
print ('</form>')
print("<a href=logout.py>Logout</a> <br>")

for image in images:
    print('<img  src="../../images/' + image +  '" width=100 height=200>' + image + '<br>')
print('<input type="submit" value="upload" onClick="location.href=location.href">')
base.finish_html