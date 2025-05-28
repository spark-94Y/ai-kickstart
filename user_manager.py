import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user (name VARCHAR(30), age INT )")
print("THE DATABASE IS CONNECTED  TO PYTHON \n" \
      "THE TABLE NAME user IS CREATED ")

def add_user() :
    name = input("ENTER THE NAME OF THE USER : ")
    age = int(input("ENTER THE AGE OF THE USER : "))
    cursor.execute("INSERT INTO user VALUES(?,?)",(name , age ))

def table():  
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    for row in rows :
        print(row)
def search_user():
    name_S = input("enter name to search user : ") 
    cursor.execute("SELECT * FROM user WHERE name = (?) ", (name_S,) )
    result = cursor.fetchall()
    if not result:
        print(f"name {name_S} not found")
    else :
      for row in result:
        print(row)
   
def delete_user():
    name_D = input("ENTER NAME TO DELETE user : ")
    cursor.execute("DELETE FROM user WHERE name = (?)",(name_D,))
    if cursor.rowcount == 0 :
        print("user not found")
    else:
      print(f"the user : {name_D} was deleted sucessfully  ")


def switch(x):
   if x == 1 :
      add_user()
   elif x == 2 :
      search_user()
   elif x == 3 :
      delete_user()
   elif x == 4 :
      table()
  
   else:
      print("enter the valild choice")
while True:
    print("CHOOSE THE COMMAND YOU WANT TO PERFROM \n" \
    "1. add user to the table \n" \
    "2. search user from the table \n" \
    "3. delete user from the table\n" \
    "4. see the table \n" \
    "5.EXIT\n") 
    choice = int(input("ENTER THE command to perform : \n"))
    if choice == 5 :
      print("exiting the program...........\n")
      break       
    else:
       switch(choice)
conn.commit()
conn.close()    
     

