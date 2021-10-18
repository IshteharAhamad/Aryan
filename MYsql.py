import mysql.connector as ms
con = ms.connect("localhost","root"," ")
cur_obj = con.cursor()
try:
    db = "create database student"
    cur_obj.execute(db)
    print("database created..")
except:
    print("somethings went wrong...")