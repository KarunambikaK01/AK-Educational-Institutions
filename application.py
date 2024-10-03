#!C:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

print("Welcome to Register My College")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fdob=form.getvalue("dob")
fphone=form.getvalue("phone")
femail=form.getvalue("email")
faddress=form.getvalue("address")
fhigh=form.getvalue("highschool")
fgpa=form.getvalue("gpa")
fsat=form.getvalue("satActScore")
fmajor=form.getvalue("major")


print("<h1>",fname,fdob,fphone,femail,faddress,fhigh,fgpa,fsat,fmajor,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="collegewp")

mycursor=mydb.cursor()
sql="INSERT INTO application(Name,DOB,Phone,Email,Address,HighSchool,GPA,SATActScore,Major) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

val=(fname,fdob,fphone,femail,faddress,fhigh,fgpa,fsat,fmajor)

mycursor.execute(sql,val)
mydb.commit()
print("Successfull")
print("</body>")
print("</html>")
