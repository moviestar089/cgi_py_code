import cgi, cgitb , mysql.connector
cgitb.enable()
print("Content-type:text/html")
print("")
mydb=mysql.connector.connect("localhost","root","root123","login")

mycursor=mydb.cursor()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('email')
passwd  = form.getvalue('psw')

sql="INSERT INTO log_table (email_, pass_) VALUES (%s, %s)"
val=(first_name, passwd)
mycursor.execute(sql,val)
mydb.commit()

