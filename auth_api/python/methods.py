# These functions need to be implemented
from flask import abort
import hashlib
import jwt
from mysqldb import gtusr_db 
sc='my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
class Token:

    def generate_token(self, username, password):
        #if username=='admin' and password=='secret':
        #sc='my2w7wjd7yXF64FIADfJxNs1oupTGAuW' #+authorization
        role=gtusr_db(username,'role')
        hashpwd=gtusr_db(username,'password')
        salt=gtusr_db(username,'salt')
        saltedpwd=password+salt
        #pwdst=str(pwd)
        pwdcry=hashlib.sha512(saltedpwd.encode()).hexdigest()
        #pwdcry=hashlib.sha512(pwd.encode()).hexdigest()
        if hashpwd==pwdcry:
        	#return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        	enc=jwt.encode({'tkn':role}, sc, algorithm='HS256')
        	return enc
        else:
        	abort (403, 'Incorrect credentials') 
        	#abort (403, hashpwd+" _VS_ "+pwdcry) 


class Restricted:

    def access_data(self, authorization):
        #sc='my2w7wjd7yXF64FIADfJxNs1oupTGAuW' #+authorization
        auth = str(authorization[7:])
        #auth = auth[7:]
        dec = jwt.decode(auth, sc, algorithms=['HS256'])
        dec = str(dec)
        rl = str(dec[4:])
        rl = rl[5:10]
        #slf = str(self)
        dec2 = jwt.decode(jwt.encode({'tkn':rl}, sc, algorithm='HS256'), sc, algorithms=['HS256'])
        dec2 = str(dec2)
        #enc = jwt.encode({'tkn':authorization}, sc, algorithm='HS256')
        #enc2 = jwt.encode({'tkn':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'}, sc, algorithm='HS256')
        #return dec+" _VS_ "+dec2
        if dec==dec2:
        	return ('You are under protected data')
        else:
        	abort (403, 'Unauthenticated')