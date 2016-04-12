import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='sql6.freesqldatabase.com',
                             user='sql6114892',
                             password='ddhIi2kbEs',
                             db='sql6114892',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = '''CREATE TABLE SINHVIEN(TenSV VARCHAR(255) DEFAULT 'noname', MaSV INT(11),NamSinh INT(4)) ENGINE = InnoDBsinhvien'''
    #     cursor.execute(sql)
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()
    #
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `SINHVIEN`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()