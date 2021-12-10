import MySQLdb as mdb

#User 
userPoints = None
updatedPoints = None

# DATABASE
SQL_HOST = "34.124.202.8"
SQL_USER = "root"
SQL_PASS = "password"
SQL_DATABASE = "innotech"

#SQL IMPLEMENTATION 
DB = mdb.connect(SQL_HOST,SQL_USER,SQL_PASS,SQL_DATABASE)

#Get input 
print("||SmartTrashCan||")
print("####FOR TESTING PURPOSES####")
print("#1 Trash = 5 POINTS#")
userName = input("User Name")
trash = input("Input Trash")

cursor = DB.cursor()

sql_GetUserPoints = f"SELECT userpoints FROM userPoints WHERE username = '{userName}'" 

cursor.execute(sql_GetUserPoints)

try: 
    cursor.execute(sql_GetUserPoints)
    DB.commit()
    print("Userpoints retrieved.")
except:
    print("Error in retrieving.")

userPoints = cursor.fetchone()

updatedPoints = int(userPoints[0]) + (int(trash) * 5)
sql_Update = f"UPDATE userPoints SET userpoints = {updatedPoints} WHERE userName = '{userName}'"

try:
    cursor.execute(sql_Update)
    DB.commit()
    print("Userpoints updated")
except: 
    print("Error in updating")


DB.close()

