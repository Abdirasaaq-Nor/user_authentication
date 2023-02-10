import mysql.connector


class Database:
    def __init__(self, host, user, passwrd, my_database):
        self.host = host
        self.user = user
        self.passwrd = passwrd
        self.database = my_database

    def create_connection(self):
        try:
            myd_database = mysql.connector.connect(
                host=self.host,  # change it with hostname your that your provider gave you
                user=self.user,  # change it with username your that your provider gave you
                passwd=self.passwrd,  # so on
                database=self.database # change it with  your own database
            )
            print("Si guul leh baabu kugu xirnay salka xogta.") # message for successfull connection
            return myd_database
        except Exception as e:
            print(e)
            return False

    def my_cursor(self):
        return self.create_connection().cursor()




mydb = Database('localhost', 'root', '12345', ' user_autho')
myDatabase = mydb.create_connection()

mycursor = myDatabase.cursor()

    # Hey my cursor go to the database and exceute this funct
# select_query = """
#                     SHOW TABLES
#     """

# mycursor.execute(select_query)
# print(mycursor.fetchall())
# ............................................................ how to create data ........................
# creatt = """

#             CREATE TABLE students(id INT AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(50) NOT NULL, user_email VARCHAR(50) NOT NULL
#             ,user_passwd VARCHAR(50) NOT NULL)
#     """
# mycursor.execute(creatt)
# ...................................................How to insert data ............................................

# sss = """
#             INSERT INTO users(user_name,user_email,user_password) VALUES(%s,%s,%s)
#     """

# mycursor.execute(sss, ('ali', 'ali@gmail.com', '87654'))
# # ineserting = """
# myDatabase.commit()
#....................................................How to update data.................................

# updd = """
#        UPDATE users SET user_name = %s WHERE id =%s
#     """
# mycursor.execute(updd, ('asmo',8))
# myDatabase.commit()

# updd2 = """
#        UPDATE users SET user_email = %s WHERE id =%s
#     """
# mycursor.execute(updd2, ('asmo@gmail.com',8))
# myDatabase.commit()

# updd3 = """
#        UPDATE users SET user_password = %s WHERE id =%s
#     """
# mycursor.execute(updd3, ('r987gvb987mbvcb',8))
# myDatabase.commit()

# ..................................................... HOW TO DELETE DATA...................................

# dddd = """
#         DELETE FROM users WHERE id = %s
#     """
# mycursor.execute(dddd, (3,))
# myDatabase.commit()

# .................................................... HOW TO SELECT DATA..........................

# sssss = """
#             SELECT user_name,user_email FROM users WHERE id = %s
#     """
# mycursor.execute(sssss,(6,))
# print(mycursor.fetchone())

# sssss2 = """
#             SELECT user_name,user_email FROM users
#     """
# mycursor.execute(sssss2)
# print(mycursor.fetchall())



# ineserting = """         INSERT INTO customers( first_name, last_name,email) VALUES(%s,%s,%s)
#  """
# mycursor.execute(ineserting,('Jaabir', 'Ali', 'Jaabir@gmail.com'))


#........deleting

# deleting = """
#         DELETE FROM customers WHERE id = %s
# """
# mycursor.execute(deleting, (7,))
# inserting deleting and updating you need to youe yourdatabase.commit()

#.............Updating

# def update_frname(first_name, user_id):
#     update_query = f"""
#                 UPDATE customers SET  first_name = %s  WHERE id = %s
#                 """
#     # cooect to the database
#     mydb = Database('localhost', 'root', '12345', 'books')
#     myDatabase = mydb.create_connection()
#     mycursor = myDatabase.cursor()
#
#     mycursor.execute(update_query, (first_name, user_id))
#     myDatabase.commit()

# update = """
#             UPDATE customers SET email = %s WHERE id = %s
#     """
# mycursor.execute(update, ('raja@gmail.com', 1))
#
# myDatabase.commit()
# update_frname('abdiraxman',1)