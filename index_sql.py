import mysql.connector as mysqlPDO

myDb = mysqlPDO.connect(
    host='localhost',
    user='root',
    password='',
    database="demo_python"
)
myCursor = myDb.cursor()
# myCursor.execute("CREATE DATABASE demo_python")
# myCursor.execute("SHOW DATABASES")
# for x in myCursor:
#   print(x)
# myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# myCursor.execute("SHOW TABLES")
# for x in myCursor:
#   print(x)
# myCursor.execute("ALTER TABLE `customers` ADD COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY AFTER `name`")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# myCursor.executemany(sql, val)

# myDb.commit()

# print(myCursor.rowcount, "was inserted.")


myCursor.execute("SELECT * FROM customers")

myResult = myCursor.fetchone()

for x in myResult:
  print(x)