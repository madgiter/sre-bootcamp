# These functions need to be implemented
from flask import abort
import hashlib
from mysqldb import gtusr_db 

class Token:

    def generate_token(self, username, password):
        #if username=='admin' and password=='secret':
        hashpwd=gtusr_db(username,'password')
        salt=gtusr_db(username,'salt')
        saltedpwd=password+salt
        #pwdst=str(pwd)
        pwdcry=hashlib.sha512(saltedpwd.encode()).hexdigest()
        #pwdcry=hashlib.sha512(pwd.encode()).hexdigest()
        if hashpwd==pwdcry:
        	return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        else:
        	abort (403, 'Incorrect credentials') 
        	#abort (403, hashpwd+" __VS__ "+pwdcry) 


class Restricted:

    def access_data(self, authorization):
	 #cad=1
        #hashlib.sha256(cad.encode()).hexdigest()
        #return authorization
        if authorization=='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c':
        	return ('You are under protected data')
        else:
        	abort (403, 'Unauthenticated')