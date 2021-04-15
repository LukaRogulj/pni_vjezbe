#!C:\Users\Support\AppData\Local\Microsoft\WindowsApps\python3.8.exe

import structure
import session
import os
import cgi

params = cgi.FieldStorage()

godina = params.getvalue("godina")
upisni_list = params.getvalue("upisni_list")
if godina is None:
    godina = "Godina1"

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()

structure.start_html()
structure.print_navigation() 

if upisni_list is not None:
    structure.print_upisni_list(data)
else:
    structure.print_subjects(data, godina)
structure.finish_html()


