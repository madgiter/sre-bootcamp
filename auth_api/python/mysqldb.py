#pip3 install flask
#pip3 install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
  host="bootcamp-tht.sre.wize.mx",
  user="secret",
  password="noPow3r",
  database="bootcamp_tht"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT username, password FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)