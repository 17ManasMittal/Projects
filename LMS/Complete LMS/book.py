import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con=sqlt.connect(host="localhost",user="root",passwd="manas2003mittal",database="library",auth_plugin="mysql_native_password")
cursor=con.cursor()
def book_input():
    try:
        bookid=input("Enter Book ID: ")
        bname=input("Enter Book Name: ")
        author=input("Enter Author Name: ")
        price=float(input("Enter Price: "))
        copies=int(input("Enter Number of Copies: "))
        qry="insert into book values({},'{}','{}',{},{},{});".format(bookid,bname,author,price,copies,copies)
        cursor.execute(qry)
        con.commit()
        print("Added Successfully")
    except:
        print("Error...Wrong Entry")
def book_edit():
    try:
        x=int(input("Enter Book ID: "))
        qry="select * from book where bookid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            y=float(input("Enter New Price: "))
            qry="update book set price={} where bookid={};".format(y,x)
            cursor.execute(qry)
            con.commit()
            print("Edited Successfully")
        else:
            print("Wrong Book ID")
    except:
        print("Error...Wrong Entry")
def book_delete():
    try:
        x=int(input("Enter Book ID: "))
        qry="select * from book where bookid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            qry="delete from book where bookid={};".format(x)
            cursor.execute(qry)
            con.commit()
            print("Deleted Successfully")
        else:
            print("Wrong Book ID")
    except:
        print("Error...Wrong Entry")
def book_search():
    try:
        x=int(input("Enter Book ID: "))
        qry="select * from book where bookid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            df=pd.read_sql(qry,con)
            print(tabulate(df,headers='keys', tablefmt='psql', showindex=False))
        else:
            print("Wrong Book ID")
    except:
        print("Error...Wrong Entry")
