import mysql.connector
lib=mysql.connector.connect(host="localhost",user="root",password="root")
cursor=lib.cursor()

if (lib.is_connected()==True):
    print ("connected successfully to mysql database")

else:
    cursor.execute("create database if not exists ")
    cursor.execute("use userlogin")
    cursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")


while True:
    print("1:Signup")
    print("2:Login")
    ch=int(input("enter your choice(SIGNUP/LOGIN(1,2))  "))
    if(ch==1):
        username=input("enter USERNAME ")
        pw=input("enter PASSWORD ")
        cursor.execute(("insert into userlogin.signup values('{}','{}')").format(username,pw))
        lib.commit()


    elif(ch==2):
        username=input("enter USERNAME")
        query=("select username from userlogin.signup where username='{}'").format(username)
        cursor.execute(query)
        p=cursor.fetchone()
        if(p is not None):
            print("VALID USERNAME ")
            pw=input("enter PASSWORD ")
            cursor.execute(("select pw from userlogin.signup where pw='{}'").format(pw))
            a=cursor.fetchone()
            if(a is not None):
                print("LOGIN SUCCESSFULL")
                break