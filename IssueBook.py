# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:07:49 2022

@author: galan
"""
import mysql.connector
import tkinter as tk
from tkinter import messagebox
import datetime

#register the transaction on the database
def checkBook():
    db=mysql.connector.connect(
       host="localhost",
       user="jonny",
       passwd="root",
       database="lsm")
    
    
    cur=db.cursor(buffered=True)
    
    sql="select status from books where bid=%s";
    val=(bidEntry.get(),)
    
    cur.execute(sql,val)
    
    check= cur.fetchone();
    if(check[0]=="available"):
        cur.close()
        return 1 
    else:
        cur.close()
        return 0

    
def issueBook():
    db=mysql.connector.connect(
       host="localhost",
       user="jonny",
       passwd="root",
       database="lsm")
    
    
    
    if(len(bidEntry.get())==0 or len(midEntry.get())==0):
        messagebox.showinfo(" ","Please enter the required parameters")
    else: 
        result=checkBook()
        today=datetime.date.today()
        if(result==1):
            cur=db.cursor()
            sql= "INSERT INTO TRANSACTIONS(bid,mid,doi,fine) VALUES(%s,%s,%s,%s)";
            book_sql="UPDATE BOOKS SET STATUS=%s where bid=%s";
            val=("issued",bidEntry.get())
            values=(bidEntry.get(),midEntry.get(),today,0.0)
            try:
                cur.execute(sql,values)
                cur.execute(book_sql,val)
                db.commit()
                messagebox.showinfo("","Book issued successfully")
                
            except mysql.connector.Error as err: 
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
                messagebox.showinfo(err)
        
        else: 
            messagebox.showinfo("","The selected book is currently unavailable")
        
        cur.close()   

def isBook():
    global  bidEntry,midEntry
    
    root = tk.Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("500x500")
        
        
    Canvas1 = tk.Canvas(root,width=500,height=500,bg="grey")
    
    Canvas1.columnconfigure([0,1],weight=1,minsize=50)
    Canvas1.rowconfigure([0,1,2],weight=1,minsize=50)
    Canvas1.pack(expand=True,fill=tk.BOTH)
    
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(headingFrame, text="ISSUE BOOK", bg='black', fg='yellow'\
                            , font=('Courier',15),height=5,width=30)
    
    headingLabel.pack()
    headingFrame.grid(row=0,column=0)
    
    mainFrame=tk.Frame(Canvas1,bg='black',width=50)
    mainFrame.columnconfigure([0,1,2],weight=1,minsize=20)
    mainFrame.rowconfigure([0,1],weight=1,minsize=20)
    
    
    bidLabel=tk.Label(mainFrame,text='Book ID: ',bg='black',fg='white',height=5\
                      ,width=15)
    bidLabel.grid(row=0,column=0)
    
    bidEntry=tk.Entry(mainFrame,width=30,selectbackground='black')
    bidEntry.grid(row=0,column=1)
    
    midLabel=tk.Label(mainFrame,text='Member ID: ',bg='black',fg='white',height=5\
                      ,width=15)
    midLabel.grid(row=1,column=0)
    
    midEntry=tk.Entry(mainFrame,width=30,selectbackground='black')
    midEntry.grid(row=1,column=1)
    
    button=tk.Button(text="Issue Book",master=Canvas1,bg='black',\
                          fg='white',relief=tk.RAISED,bd=5,height=5,width=20,\
                              command=issueBook)
    butt=tk.Button(text='Exit',master=Canvas1,bg='black',fg='white',relief=tk.RAISED\
                   ,bd=5,height=5,width=20,command=root.destroy)
        
    mainFrame.grid(row=1,column=0)
    
    button.grid(row=2,column=0,sticky='w')
    butt.grid(row=2,column=1,sticky='e')
    root.mainloop()
    
    
    