import db 
import password_utils

def register(username, password, email, secret_question, secret_answer):
    user_id = db.create_user(username, password, email, secret_question, secret_answer)
    if user_id:
        return True
    else:
        return False
        
def authenticate(username, password):
    user = db.get_user(username)
    if (user and password_utils.verify_password(password, user[2])):
        return True, user[0]
    else:
        return False, None
        
def change_password(username, new_password):
    db.update_user_password(username, new_password)
