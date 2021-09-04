#pip3 install flask
#pip3 install mysql-connector-python
import mysql.connector

def gtusr_db(uname,field):
	mydb = mysql.connector.connect(
  		host="bootcamp-tht.sre.wize.mx",
  		user="secret",
  		password="noPow3r",
  		database="bootcamp_tht"
		)

	mycursor = mydb.cursor()
	mycursor.execute("SELECT "+field+" FROM users WHERE username ='"+uname+"'")
	myresult = mycursor.fetchone()
	return str(myresult[0])
	#return myresult
