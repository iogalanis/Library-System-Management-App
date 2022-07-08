# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:43:29 2021

@author: galan
"""
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from tkinter import ttk
from addBooks import addBook
from addMember import addmember
from UpdateBook import bid
from IssueBook import isBook
from returnBook import retBook
from updateMember import mid


#Function to put the results of the search query in display
def packMember(result,treeFrame):
    for item in treeFrame.winfo_children():
        item.destroy()
        
    columns=('student_name','book_name','price','issue_date','return_date')
    tree=ttk.Treeview(treeFrame,columns=columns,show='headings') 
    
    tree.heading('student_name',text='mid')
    tree.column('student_name', width=200,stretch=True)
    tree.heading('book_name',text='Name')
    tree.column('book_name', width=200,stretch=True)
    tree.heading('price',text='Class')
    tree.column('price', width=100,stretch=True)
    tree.heading('issue_date',text='Phone')
    tree.column('issue_date', width=100,stretch=True)
    tree.heading('return_date',text='Email')
    tree.column('return_date', width=100,stretch=True)
    
    for row in result:
        tree.insert('', tk.END, values=row)
    
    tree.grid(row=0,column=0)
    
    scrollbar=ttk.Scrollbar(treeFrame,orient=tk.VERTICAL,command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0,column=1,sticky='nsw')
    
    
#function to display the results of search Books
def packBook(result,treeFrame):
    for item in treeFrame.winfo_children():
        item.destroy()
    
    
    columns=('student_name','book_name','price','issue_date','return_date')
    tree=ttk.Treeview(treeFrame,columns=columns,show='headings')        
    
    tree.heading('student_name',text='bid')
    tree.column('student_name', width=200,stretch=True)
    tree.heading('book_name',text='Title')
    tree.column('book_name', width=200,stretch=True)
    tree.heading('price',text='Author')
    tree.column('price', width=100,stretch=True)
    tree.heading('issue_date',text='Price')
    tree.column('issue_date', width=100,stretch=True)
    tree.heading('return_date',text='Status')
    tree.column('return_date', width=100,stretch=True)
    
    for row in result:
        tree.insert('', tk.END, values=row)
    
    tree.grid(row=0,column=0)
    
    scrollbar=ttk.Scrollbar(treeFrame,orient=tk.VERTICAL,command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0,column=1,sticky='nsw')
    
    refreshButton=tk.Button(treeFrame,text='Refresh Transactions',bg='black',fg='white'\
                        ,bd=5,height=-15,width=20,command=lambda:tView(treeFrame))

    refreshButton.grid(row=0,column=2,sticky='nw')

#Function to fetch the results of transactions
def getT():
    db=mysql.connector.connect(
        host="localhost",
        user="jonny",
        passwd="root",
        database="lsm")
    
    cur=db.cursor()
    
    sql="Select name,title,price,doi,dor\
        From books as b,members as m,transactions as t\
        where b.bid=t.bid and m.mid=t.mid\
        Group by name";
    
    cur.execute(sql)
    
    result=cur.fetchall()
    
    cur.close()
    return result
    
    
#Function to display the results of transactions
def tView(treeFrame):
    columns=('student_name','book_name','price','issue_date','return_date')
    
    tree=ttk.Treeview(treeFrame,columns=columns,show='headings')        
    
    tree.heading('student_name',text='Student')
    tree.column('student_name', width=200,stretch=True)
    tree.heading('book_name',text='Book')
    tree.column('book_name', width=200,stretch=True)
    tree.heading('price',text='Price')
    tree.column('price', width=100,stretch=True)
    tree.heading('issue_date',text='Issue Date')
    tree.column('issue_date', width=100,stretch=True)
    tree.heading('return_date',text='Return Date')
    tree.column('return_date', width=100,stretch=True)
    
    result=getT()
    
    for row in result:
        tree.insert('', tk.END, values=row)
    
    tree.grid(row=0,column=0)
    
    scrollbar=ttk.Scrollbar(treeFrame,orient=tk.VERTICAL,command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0,column=1,sticky='nsw')
    
    refreshButton=tk.Button(treeFrame,text='Refresh Transactions',bg='black',fg='white'\
                        ,bd=5,height=-15,width=20,command=lambda:tView(treeFrame))

    refreshButton.grid(row=0,column=2,sticky='nw')

#function to fetch the results of find member
def findMember(treeFrame):
    db=mysql.connector.connect(
        host="localhost",
        user="jonny",
        passwd="root",
        database="lsm")
    
    cur=db.cursor()
    
    find=sMemberEntry.get()
    find=find.split(",")
    
    if(len(find)<1):
        messagebox.showinfo("","Please enter a name or class")
        return
    elif(len(find)==1):
        sql="SELECT max(mid) mid,name,class,phone,email FROM Members WHERE \
            name like %s or class like %s group by name,class,phone,email"
        values=(find[0],find[0])

    
    elif(len(find)==2):
        sql="SELECT max(mid) mid,name,class,phone,email FROM members WHERE\
            name like %s and class like %s group by name,class,phone,email"
        values=(find[0],find[1])
        
    try:
         cur.execute(sql,values)
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        messagebox.showinfo("",err)
    
    result=cur.fetchall()
    packMember(result,treeFrame)
    cur.close()
    

#function to fetch the results of search book
def searchBooks(treeFrame):
    db=mysql.connector.connect(
        host="localhost",
        user="jonny",
        passwd="root",
        database="lsm")
    
    cur=db.cursor()
    
    
    
    search=sBookEntry.get()
    search=search.split(",")
    
    if(len(search)<1):
        messagebox.showinfo("","Please enter a title,author or status of the book")
        return
    elif(len(search)==1):
        sql="SELECT max(bid) bid,title,Author,price,status FROM BOOKS WHERE \
            title Like %s or Author like %s\
            or status like %s group by title,Author,price,status"
        values=(search[0],search[0],search[0])

    
    elif(len(search)==2):
        sql="SELECT max(bid) bid,title,Author,price,status FROM BOOKS WHERE\
            title like %s and Author like %s group by title,Author,price,status"
        print(1)
        values=(search[0],search[1])
        
    elif(len(search)==3):
        sql="SELECT max(bid) bid,title,Author,price,status FROM BOOKS WHERE\
            title like %s and Author like %s and status like %s group by \
                title,Author,price,status"
                
        values(search[0],search[1],search[2])
    
    try:
         cur.execute(sql,values)
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        messagebox.showinfo("",err)
    
    result=cur.fetchall()
    packBook(result,treeFrame)
    cur.close()

root = tk.Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("1000x1000")

Canvas1 = tk.Canvas(root,width=1000,height=1000,bg="grey")
Canvas1.columnconfigure([0],weight=1,minsize=100)
Canvas1.rowconfigure([0,1,2,3],weight=1,minsize=100)
Canvas1.pack(expand=True,fill=tk.BOTH)


headingFrame=tk.Frame(Canvas1,bg='grey',bd=5)
headingLabel=tk.Label(headingFrame,text='Library System Management',bg='grey'\
                      ,fg='black', font=('Courier',20),height=2,width=30)
headingLabel.pack()
headingFrame.grid(row=0,column=0)
    
#FRAME FOR SEARCHING BOOKS OR MEMBERS,RESULTS ARE SHOWN ON THE BOX BELOW

searchFrame=tk.Frame(Canvas1,bg='grey')
searchFrame.columnconfigure([0,1,2],weight=1,minsize=100)
searchFrame.rowconfigure([0,1],weight=1,minsize=100)

sBookLabel=tk.Label(searchFrame,text='Search Book(by Title,Author,status): ',\
                    bg='grey',fg='black',\
                    height=2,width=40,font=('Courier',10))
sBookLabel.grid(row=0,column=0)

sMemberLabel=tk.Label(searchFrame,text='Search Member(by Name,Class): ',bg='grey'\
                      ,fg='black',\
                      height=2,width=30,font=('Courier',10))
sMemberLabel.grid(row=1,column=0)

sBookEntry=tk.Entry(searchFrame,width=50,selectbackground='grey')
sBookEntry.grid(row=0,column=1)

sMemberEntry=tk.Entry(searchFrame,width=50,selectbackground='grey')
sMemberEntry.grid(row=1,column=1)

searchButton=tk.Button(searchFrame,text='Search',bg='black',fg='white',relief\
                       =tk.RAISED,bd=5,height=1,width=10,command=lambda:searchBooks(treeFrame))
searchButton.grid(row=0,column=2)

findButton=tk.Button(searchFrame,text='Find',bg='black',fg='white',relief=\
                     tk.RAISED,bd=5,height=1,width=10,command=lambda:findMember(treeFrame))
findButton.grid(row=1,column=2)

searchFrame.grid(row=1,column=0)

#FRAME FOR THE MAIN FUNCTION BUTTONS 

buttonFrame=tk.Frame(Canvas1,bg='grey',width=50)
buttonFrame.columnconfigure([0,1,2],weight=1,minsize=50)
buttonFrame.rowconfigure([0,1],weight=1,minsize=30)


addBooksbutton= tk.Button(text="Add Book",master=buttonFrame,bg='black',\
                          fg='white',relief=tk.RAISED,bd=5,height=2,width=15,\
                              command=addBook)
addMembersbutton=tk.Button(text="Add Member",master=buttonFrame,bg='black',\
                           fg='white',relief=tk.RAISED,bd=5,height=2,width=15\
                               ,command=addmember)
updateBookbutton=tk.Button(text="Update Book Details",master=buttonFrame,\
                           bg='black',fg='white',relief=tk.RAISED,bd=5,height=2,\
                               width=15,command=bid)
updateMemberbutton=tk.Button(text="Update Member Details",master=buttonFrame,\
                             bg='black',fg='white',relief=tk.RAISED,bd=5,\
                                 height=2,width=15,command=mid)
issueBookbutton=tk.Button(text="Issue Book",master=buttonFrame,bg='black',\
                          fg='white',relief=tk.RAISED,bd=5,height=2,width=15\
                              ,command=isBook)
returnBook=tk.Button(text="Return Book",master=buttonFrame,bg='black',fg='white',\
                     relief=tk.RAISED,bd=5,height=2,width=15,command=retBook)

addBooksbutton.grid(row=0,column=0,padx=20,pady=10)
addMembersbutton.grid(row=1,column=0,padx=20,pady=10)
updateBookbutton.grid(row=0,column=1,padx=20,pady=10)
updateMemberbutton.grid(row=1,column=1,padx=20,pady=10)
issueBookbutton.grid(row=1,column=2,padx=20,pady=10)
returnBook.grid(row=0,column=2,padx=20,pady=10)

buttonFrame.grid(row=2,column=0)

treeFrame=tk.Frame(Canvas1,bg='grey')
treeFrame.columnconfigure([0,1,2],weight=1,minsize=100)
treeFrame.rowconfigure([0],weight=1,minsize=100)

tView(treeFrame)

refreshButton=tk.Button(treeFrame,text='Refresh Transactions',bg='black',fg='white'\
                        ,bd=5,height=-15,width=20,command=lambda:tView(treeFrame))

refreshButton.grid(row=0,column=2,sticky='nw')
treeFrame.grid(row=3,column=0)
root.mainloop()
