import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root",passwd="manas2003mittal",database="library",auth_plugin="mysql_native_password")
cursor=con.cursor()
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
