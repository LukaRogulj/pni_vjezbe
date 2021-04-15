#!C:\Users\Support\AppData\Local\Microsoft\WindowsApps\python3.8.exe
import model
count = 0

def start_html():
    print('''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>vjezba4</title>

        </head>
        <body>
        ''')

def print_navigation():
    print ('''
    <form action="" method="post">
    <div id="navigation">
        <input type="submit" name="godina" value="Godina1" formaction="index.py">
        <input type="submit" name="godina" value="Godina2" formaction="index.py">
        <input type="submit" name="godina" value="Godina3" formaction="index.py">
        <input type="submit" name ="upisni_list" value="Upisni list" formaction="index.py">
    </div>''')


def print_subjects(data, year):


    print("<table>")
    print("<tr><td>", year,"</td></tr>")
    print("<tr><td align ='center'>Predmet</td><td align='center'>Status</td><td align='center'>Bodovi</td></tr>")

    subjects = model.get_subjects()

    for key, subject in subjects.items():
        subject_year = subject.get('year', 'n/a')

        if str(subject_year) == year[6]:
            check1 = check2 = check3 = ""
            subject_name = subject.get('name', 'n/a')
            subject_ects = subject.get('ects', 'n/a')

            status = model.check(data, key)

            if status == "Ne upisuje":
                check1 = "checked"
            elif status == "Upisuje":
                check2 = "checked"
            elif status == "Polozen":
                check3 = "checked"

            temp = ""

            print("""
                <tr>
                    <td>""", subject_name,"""</td>
                    <td>
                        <input type='radio' name=""", key,""" value='Ne upisuje'""",check1,""" """,temp,""">Ne Upisuje
                        <input type='radio' name=""", key,""" value='Upisuje'""",check2,""" """,temp,""">Upisuje
                        <input type='radio' name=""", key,""" value='Polozen'""",check3,""" """,temp,""">Polozen
                    </td>
                    <td align='center'>""", subject_ects,"""</td>
                </tr>
                """)

    print("</table>")

def print_upisni_list(data):
    print("<table>")
    print("<tr><td align = 'center'>Predmet</td><td>Status</td><td>Bodovi</td></tr>")

    subjects = model.get_subjects()
    for subject_id, status in data.items():
        if subject_id != "upisni_list":
            subject_name = subjects.get(subject_id, {}).get("name", "n/a")
            subject_ects = subjects.get(subject_id, {}).get("ects", "n/a")
            print ("<tr><td>", subject_name,"</td><td>", status,"</td><td align='center'>"
                , subject_ects,"</td></tr>")
    print("</table>")

def finish_html():
    print('''
    </form>
    </body>
    </html>
    ''')
