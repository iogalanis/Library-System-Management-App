# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 18:45:58 2022

@author: galan
"""
import mysql.connector
import tkinter as tk
from tkinter import messagebox

def memReg():
    db=mysql.connector.connect(
        host="localhost",
        user="jonny",
        passwd="root",
        database="lsm")
    
    
    cur=db.cursor()
    
    if(len(name.get())==0 or len(cl.get())==0 or len(address.get())==0\
           or len(phone.get())==0 or len(email.get())==0):
       messagebox.showinfo("Please fill all the required parameters")
    
    else: 
        memberName=name.get()
        memberClass=cl.get()
        memberAddress=address.get()
        memberPhone=phone.get()
        memberEmail=email.get()
    
    
        insertMember='insert into members(name,class,address,phone,email) \
            values(%s,%s,%s,%s,%s)';
        values=(memberName,memberClass,memberAddress,memberPhone,memberEmail)
        
        try:
            cur.execute(insertMember,values)
            db.commit()
            messagebox.showinfo('Success',"Member added successfully")
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            messagebox.showinfo(err)
    cur.close()     

def addmember():
    
    global mid,name,cl,address,phone,email
    
    root = tk.Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1000x1000")
    
    
    Canvas1 = tk.Canvas(root,width=1000,height=1000,bg="blue")

    Canvas1.pack(expand=True,fill=tk.BOTH)
    
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(Canvas1, text="Add Members", bg='black', fg='yellow'\
                            , font=('Courier',15),height=5,width=30)
    
    headingLabel.pack()
    headingFrame.pack()
    
    mainFrame=tk.Frame(Canvas1,bg='black',width=50)
    
    mainFrame.columnconfigure([0,1],weight=1,minsize=50)
    mainFrame.rowconfigure([0,1,2,3,4,5],weight=1,minsize=50)

    
    #NAME 
    
    nameLabel=tk.Label(mainFrame,text='Name: ',bg='black',fg='white',height=5\
                       ,width=13)
    nameLabel.grid(row=1,column=0)
    
    name=tk.Entry(mainFrame,width=50,selectbackground='black')
    name.grid(row=1,column=1)
    
    #CLASS
    
    classLabel=tk.Label(mainFrame,text='Class: ',bg='black',fg='white',height=5\
                        ,width=13)
    classLabel.grid(row=2,column=0)
    
    cl=tk.Entry(mainFrame,width=50,selectbackground='black')
    cl.grid(row=2,column=1)
    
    #ADDRESS
    
    addressLabel=tk.Label(mainFrame,text='Address: ',bg='black',fg='white'\
                          ,height=5,width=13)
    addressLabel.grid(row=3,column=0)
    
    address=tk.Entry(mainFrame,width=50,selectbackground='black')
    address.grid(row=3,column=1)
    
    #PHONE
    
    phoneLabel=tk.Label(mainFrame,text='Phone: ',bg='black',fg='white',height=5,\
                        width=13)
        
    phoneLabel.grid(row=4,column=0)
    
    phone=tk.Entry(mainFrame,width=50,selectbackground='black')
    phone.grid(row=4,column=1)
    
    #EMAIL

    emailLabel=tk.Label(mainFrame,text='Email: ',bg='black',fg='white',height=5\
                        ,width=13)
    emailLabel.grid(row=5,column=0)
    email=tk.Entry(mainFrame,width=50,selectbackground='black')
    email.grid(row=5,column=1)
    
    ButtonFrame=tk.Frame(Canvas1,bg="blue")
    ButtonFrame.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11],weight=1,minsize=50)
    ButtonFrame.rowconfigure([0],weight=1,minsize=50)
    
    submitButton=tk.Button(ButtonFrame,text='Submit',bg='black',fg='white'\
                           ,relief=tk.RAISED,bd=5,height=5,width=30,command=memReg)\
        .grid(row=0,column=2)
        
    exitButton=tk.Button(ButtonFrame,text='Exit',bg='black',fg='white'\
                         ,relief=tk.RAISED,bd=5,height=5,width=30,command=root.destroy)\
        .grid(row=0,column=10)
    
    mainFrame.pack()
    
    ButtonFrame.pack(side=tk.LEFT)
    
    root.mainloop()
    
    
    
    