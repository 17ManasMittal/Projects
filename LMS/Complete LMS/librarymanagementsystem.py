import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root",passwd="manas2003mittal",database="library")
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
def member_input():
    try:
        memberid=int(input("Enter Member ID: "))
        mname=input("Enter Member Name: ")
        madd=input("Enter Member Address: ")
        phone=input("Enter Phone Number: ")
        qry="insert into member values({},'{}','{}','{}');".format(memberid,mname,madd,phone)
        cursor.execute(qry)
        con.commit()
        print("Added Successfully")
    except:
        print("Error...Wrong Entry")
def member_edit():
    try:
        x=int(input("Enter Member ID: "))
        qry="select * from member where memberid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            y=input("Enter New Address: ")
            qry="update member set madd='{}' where memberid={};".format(y,x)
            cursor.execute(qry)
            con.commit()
            print("Edited Successfully")
        else:
            print("Wrong Member ID")
    except:
        print("Error...Wrong Entry")
def member_delete():
    try:
        x=int(input("Enter Member ID: "))
        qry="select * from member where memberid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            qry="delete from member where memberid={};".format(x)
            cursor.execute(qry)
            con.commit()
            print("Deleted Successfully")
        else:
            print("Wrong Member ID")
    except:
        print("Error...Wrong Entry")
def member_search():
    try:
        x=int(input("Enter Member ID: "))
        qry="select * from member where memberid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            df=pd.read_sql(qry,con)
            print(tabulate(df,headers='keys', tablefmt='psql', showindex=False))
        else:
            print("Wrong Member ID")
    except:
        print("Error...Wrong Entry")

def book_issue():
    try:
        q="select max(issueid) from issue;"
        cursor.execute(q)
        r=cursor.fetchone()[0]
        if r:
            issueid=r+1
        else:
            issueid=1
        x=int(input("Enter Member ID: "))
        q1="select * from member where memberid={};".format(x)
        cursor.execute(q1)
        r=cursor.fetchone()
        if r:
            y=int(input("Enter Book ID: "))
            q2="select bookid,rem_copies from book where bookid={};".format(y)
            cursor.execute(q2)
            r=cursor.fetchone()
            if r:
                if r[1]>0:
                    issuedate=input("Enter Issue Date: ")
                    copies=int(input("Enter Number of Copies: "))
                    remcopies=r[1]-copies
                    q3="insert into issue values({},'{}',{},{},{});".format(issueid,issuedate,x,y,copies)
                    cursor.execute(q3)
                    q4="update book set rem_copies={} where bookid={};".format(remcopies,y)
                    cursor.execute(q4)
                    con.commit()
                    print("Book Issued")
                else:
                    print("Book is not Available")
            else:
                print("Wrong Book ID")
        else:
            print("Wrong Member ID")
    except:
        print("Error...Wrong Entry")
def book_return():
    try:
        q="select max(returnid) from returns;"
        cursor.execute(q)
        r=cursor.fetchone()[0]
        if r:
            returnid=r+1
        else:
            returnid=1
        x=int(input("Enter Member ID: "))
        q1="select * from member where memberid={};".format(x)
        cursor.execute(q1)
        r=cursor.fetchone()
        if r:
            y=int(input("Enter Book ID: "))
            q2="select bookid,rem_copies from book where bookid={};".format(y)
            cursor.execute(q2)
            r=cursor.fetchone()
            if r:
                returndate=input("Enter Return Date: ")
                copies=int(input("Enter Number of Copies: "))
                remcopies=r[1]+copies
                q3="insert into returns values({},'{}',{},{},{});".format(returnid,returndate,x,y,copies)
                cursor.execute(q3)
                q4="update book set rem_copies={} where bookid={};".format(remcopies,y)
                cursor.execute(q4)
                con.commit()
                print("Book Returned")
            else:
                print("Wrong Book ID")
        else:
            print("Wrong Member ID")
    except:
        print("Error...Wrong Entry")
def book_output():
    df=pd.read_sql("select * from book",con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
def member_output():
    df=pd.read_sql("select * from member",con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
def return_output():
    df=pd.read_sql("select * from returns",con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
def issue_output():
    df=pd.read_sql("select * from issue",con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
def col_chart():
    q="select bookid,count(copies) as totalcopies from issue group by bookid;"
    df=pd.read_sql(q,con)
    print(df)
    plt.bar(df.bookid,df.totalcopies)
    plt.xlabel("BookID")
    plt.ylabel("Copies Issued")
    plt.title("Best Reading Book")
    plt.xticks(df.bookid)
    plt.show()
while(True):
    print("="*80)
    print("\t\t\t------Library Management System------\n")
    print("="*80)
    print("\t\t\t\tEnter your choice\n\t\t\t\t1. Book Details\n\t\t\t\t2. Member Details\n\t\t\t\t\
3. Transaction\n\t\t\t\t4. Report\n\t\t\t\t5. Exit")
    choice=int(input())
    if choice==1:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Add Book Details\n\t\t\t\t2. Edit Book Details\n\t\t\t\t\
3. Delete a Book\n\t\t\t\t4. Search a Book\n\t\t\t\t5. Back to Main Menu")
            ch=int(input())
            if ch==1:
               book_input()
            elif ch==2:
               book_edit()
            elif ch==3:
               book_delete()
            elif ch==4:
               book_search()
            elif ch==5:
                break
    elif choice==2:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Add Member Details\n\t\t\t\t\
2. Edit Member Details\n\t\t\t\t3. Delete a Member\n\t\t\t\t4. Search a Member\n\t\t\t\t5. Back to Main Menu")
            ch=int(input())
            if ch==1:
                member_input()
            elif ch==2:
                member_edit()
            elif ch==3:
                member_delete()
            elif ch==4:
                member_search()
            elif ch==5:
                break
    elif choice==3:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Issue Book\n\t\t\t\t\
2. Return Book\n\t\t\t\t3. Back to Main Menu")
            ch=int(input())
            if ch==1:
                book_issue()
            elif ch==2:
                book_return()
            elif ch==3:
                break
    elif choice==4:
        while(True):
            print("\t\t\t\tEnter your choice\n\t\t\t\t1. Book Details\n\t\t\t\t2. Member Details\n\t\t\t\t\
3. Issue Details\n\t\t\t\t4. Return Details\n\t\t\t\t5. Best reading Book(Chart)\n\t\t\t\t6. Back To Main Menu\n")
            ch=int(input())
            if ch==1:
                book_output()
            elif ch==2:
                member_output()
            elif ch==3:
                issue_output()
            elif ch==4:
                return_output()
            elif ch==5:
                col_chart()
            elif ch==6:
                break
    elif choice==5:
        break
