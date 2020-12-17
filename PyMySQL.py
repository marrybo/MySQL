import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Borisova21_',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    cursor.execute("select * FROM tab;")
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute("insert into tab (`Id`,`Name`,`Age`) values (7, 'Леонид', 17);")
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute("update tab set `Name` = 'Коля',`Age` = '20' where (`Id`= 2);")
    connection.commit()
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute("select `Name` FROM tab WHERE `Age`<=18;")
    print(cursor.fetchall())

with connection.cursor() as cursor:
    cursor.execute("delete FROM tab WHERE `Age`<=18;")
    connection.commit()
    print(cursor.fetchall())

connection.close()
