import sqlite3
con = sqlite3.connect("text.db")
cob = con.cursor()
#cob.execute("create table student12(Roll_No INTEGER PRIMARY KEY,name VARCHAR(20),Branch VARCHAR ,Year DATE,Address TEXT,Mobile INTEGER)")
#cob.execute("insert into student12 values(1,'king khan','IT',2017,'Bahaduri' ,999033844)")
#cob.execute("insert into student12 values(?,?,?,?,?,?)",(3,'shiv dutt','computer science','2017','Azam garh',935479418))
cob.execute("UPDATE student12 SET Address='Gorakhpur' WHERE Roll_No=1")
con.commit()
  
cob.close()
con.close()