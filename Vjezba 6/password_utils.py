import os
import hashlib
import base64

def hash_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    hash = salt + key 
    """print ("")
    print("salt")
    print (salt)
    print ("salt encoded")
    print (salt.encode())"""

    return hash

def verify_password (password, hash):
 
    salt = hash[:32]
    key = hash[32:]

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'), 
        salt, 
        100000)
    return new_key == key 