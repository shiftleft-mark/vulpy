from flask import Blueprint, render_template, redirect

mod_hello = Blueprint('mod_hello', __name__, template_folder='templates')

@mod_hello.route('/')
def do_hello():
    return 'hello :)'


#Mark and Mike test code

import hashlib
import os

salt = os.urandom(32) # Remember this
password = 'FINDMYSECRET'

key = hashlib.pbkdf2_hmac(
    'sha256', # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt, # Provide the salt
    100000 # It is recommended to use at least 100,000 iterations of SHA-256 
)

#end code
