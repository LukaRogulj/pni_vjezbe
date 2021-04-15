import mysql.connector # "C:\Program Files\Python 3.5\python.exe" -m pip install mysql-connector 

import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name": "autorization_project",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def create_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 

def get_user_by_username(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = cursor.fetchone()
    return myresult

def get_user(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult

def get_users():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    return myresult

def get_user_role(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT roles.role FROM roles JOIN users ON users.role_id = roles.role_id WHERE users.user_id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult[0]

def delete_user(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM users WHERE user_id='" + str(user_id) + "'")
    mydb.commit()

def update_user(user_id, username, gender, role_id):
    query = "UPDATE users SET username=%s, gender=%s, role_id=%s  WHERE user_id='" + str(user_id) + "'"
    values = (username, gender, role_id)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_role(role_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM roles WHERE role_id='" + str(role_id) + "'")
    myresult = cursor.fetchone()
    return myresult