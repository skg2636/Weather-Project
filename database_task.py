import pymysql as sql
from password_task import encryptPassword

def db_connection():
    """This function is used to create connection with database"""
    conn = sql.connect(host='localhost',user='root',password='Sandeep123',database='python_db')
    cursor = conn.cursor()
    return conn,cursor

def checkUser(email):
    cmd = f"select * from task1 where email= '{email}';"
    db, cursor = db_connection()
    cursor.execute(cmd)
    data = cursor.fetchone()
    if data:
        return "User Exits"
    else:
        return "New User"


def insertUserDetails(data):
    name = data['name']
    email = data['email']
    password = data['password']
    address = data['address']
    gender = data['gender']
    cmd = f"insert into task1 values('{email}','{password}','{name}','{address}','{gender}');"
    try:
        db, cursor = db_connection()
        cursor.execute(cmd)
        db.commit()
        return True,"Registered"
    except Exception as err:
        return False,"Database Error"

def userLogin(email,password):
    result = checkUser(email)
    enc_pass = encryptPassword(password)
    if result == "User Exits":
        cmd = f"select * from task1 where email = '{email}' and password = '{enc_pass}';"
        db,cursor = db_connection()
        cursor.execute(cmd)
        data = cursor.fetchone()
        if data:
            return True,"Login Successful"
        else:
            return False, "Wrong Password"

    else:
        return False,"User does not exists"
