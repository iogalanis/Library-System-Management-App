# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 20:26:44 2022

@author: galan
"""
import mysql.connector
import tkinter as tk
from tkinter import messagebox

def deleteReg():
    db=mysql.connector.connect(
      host="localhost",
      user="jonny",
      passwd="root",
      database="lsm")
    
    
    cur=db.cursor()
    
    sql ='DELETE FROM transactions where bid=%s'
    
    sql1='DELETE FROM books WHERE bid =%s'
    val=(bookid,)

    try:
        cur.execute(sql,val)
        cur.execute(sql1,val)
        db.commit()
        messagebox.showinfo("Deleted successfully")
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        messagebox.showinfo(err)
    
    cur.close()
    

def choice():
    global bookid
    bookid =idEntry.get()
    
    if(len(bookid)==0):
        messagebox.showinfo("","Please enter a correct book id")
        root.destroy()
        bid()
        
        return
    
    for widgets in Canvas1.winfo_children():
        widgets.destroy()
    
    
    Canvas1.columnconfigure([0],weight=1,minsize=50)
    Canvas1.rowconfigure([0,1,2],weight=1,minsize=50)
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(headingFrame, text="Select option: ", \
                        bg='black', fg='yellow', font=('Courier',15),height=5,width=30)
    
    headingLabel.pack()
    headingFrame.grid(row=0,column=0)
    

    mainFrame=tk.Frame(Canvas1,bg='black',width=50)
    mainFrame.columnconfigure(0,weight=1,minsize=50)
    mainFrame.rowconfigure([0,1],weight=1,minsize=30)
    
    buttonFrame=tk.Frame(Canvas1,bg='black',width=50)
    
    updateBooksbutton= tk.Button(text="Update Book Details",master=mainFrame,bg='black',\
                          fg='white',relief=tk.RAISED,bd=5,height=5,width=30,command=updateBook)
    
    deleteBookbutton=tk.Button(mainFrame,text='Delete Book',bg='black',fg='white'\
                               ,relief=tk.RAISED,bd=5,height=5,width=30,command=deleteReg)
    
    
    updateBooksbutton.grid(row=0,column=0)
    deleteBookbutton.grid(row=1,column=0)
    
    exitButton=tk.Button(buttonFrame,text='Exit',bg='black',fg='white',relief\
                         =tk.RAISED,bd=5,height=5,width=30,command=root.destroy)
    exitButton.pack()
    
    mainFrame.grid(row=1,column=0)
    
    buttonFrame.grid(row=2,column=0,sticky='e')



def optionReg(entry,row):
    db=mysql.connector.connect(
       host="localhost",
       user="jonny",
       passwd="root",
       database="lsm")
    
    
    cur=db.cursor()
    
    newEntry=entry.get()
    print(newEntry)
    if(len(newEntry)==0):
        messagebox.showinfo("","Please enter the desired value")
    
    else:
    
        sql =str("UPDATE books SET " + row + "= %s WHERE bid = %s")
        val=(newEntry,bookid)
        
        
        try:
            cur.execute(sql,val)
            db.commit()
            messagebox.showinfo("Updated successfully")
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            messagebox.showinfo(err)
        
    cur.close()
    
def option(value):

    for widgets in Canvas1.winfo_children():
        widgets.destroy()
    
    
    Canvas1.columnconfigure([0],weight=1)
    Canvas1.rowconfigure([0,1,2],weight=1)
    
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(headingFrame, text="Insert the desired value ", \
                        bg='black', fg='yellow', font=('Courier',15),height=5,\
                            width=30)
    
    headingFrame.grid(row=0,column=0)
    headingLabel.pack()
    
    mainFrame=tk.Frame(Canvas1,bg='black',width=50)
    
    mainFrame.columnconfigure([0,1],weight=1,minsize=50)
    mainFrame.rowconfigure([0],weight=1,minsize=50)
    
  
    
    if(value==1):
        lbl=tk.Label(mainFrame,text='New Title: ',bg='black',fg='white'\
                      ,height=5,width=30) 
        row='title'
    
    if(value==2):
        lbl=tk.Label(mainFrame,text='New Author: ',bg='black',fg='white'\
                     ,height=5,width=30)
        row='Author'
        
    if(value==3):
        lbl=tk.Label(mainFrame,text='New page number: ',bg='black',fg='white'\
                     ,height=5,width=30)
        row='pages'
            
    if(value==4):
        lbl=tk.Label(mainFrame,text='New price number: ',bg='black',fg='white'\
                     ,height=5,width=30)
        row='price'
    
    if(value==5):
        lbl=tk.Label(mainFrame,text='New publisher: ',bg='black',fg='white'\
                     ,height=5,width=30)
        
        row='publisher'
        
    if(value==6):
        lbl=tk.Label(mainFrame,text='New edition number: ',bg='black',fg='white'\
                     ,height=5,width=30)
        
        row='edition'
    
    lbl.grid(row=0,column=0)
    
    entry=tk.Entry(mainFrame,width=50,selectbackground='black')
    entry.grid(row=0,column=1)
    
    mainFrame.grid(row=1,column=0)
    
    ButtonFrame=tk.Frame(Canvas1,bg="green")
    ButtonFrame.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11],weight=1,minsize=50)
    ButtonFrame.rowconfigure([0],weight=1,minsize=50)
    
    submitButton=tk.Button(ButtonFrame,text='Submit',bg='black',fg='white'\
                           ,relief=tk.RAISED,bd=5,height=5,width=30,command=lambda:optionReg(entry,row))\
        .grid(row=0,column=2,sticky='e')
        
    exitButton=tk.Button(ButtonFrame,text='Back',bg='black',fg='white'\
                         ,relief=tk.RAISED,bd=5,height=5,width=30,command=root.destroy)\
        .grid(row=0,column=10,sticky='w')
    ButtonFrame.grid(row=3,column=0)
           
def bid():
    global root,Canvas1,idEntry
    
    root = tk.Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1000x1000") 
    
    Canvas1 = tk.Canvas(root,width=1000,height=1000,bg="green")
    Canvas1.rowconfigure([0,1,2],weight=1)
    Canvas1.columnconfigure([0],weight=1)
    Canvas1.pack(expand=True,fill=tk.BOTH)
    
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(headingFrame, text="Please enter the book id", \
                        bg='black', fg='yellow', font=('Courier',15),height=5,\
                            width=30)
    
    headingLabel.pack()
    headingFrame.grid(row=0,column=0)
    
    mainFrame=tk.Frame(Canvas1,bg='black',width=50)    
    mainFrame.columnconfigure([0,1],weight=1,minsize=50)
    mainFrame.rowconfigure([0],weight=1,minsize=50)
    
    
    idLabel=tk.Label(mainFrame,text='Book ID: ',bg='black',fg='white',height=10\
                     ,width=13)
    idLabel.grid(row=0,column=0)
    
    idEntry=tk.Entry(mainFrame,width=50,selectbackground='black')
    idEntry.grid(row=0,column=1)
    
    
    ButtonFrame=tk.Frame(Canvas1,bg="green")
    ButtonFrame.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11],weight=1,minsize=50)
    ButtonFrame.rowconfigure([0],weight=1,minsize=50)
    
    submitButton=tk.Button(ButtonFrame,text='Submit',bg='black',fg='white'\
                           ,relief=tk.RAISED,bd=5,height=5,width=30,command=choice)\
        .grid(row=0,column=2,sticky='e')
        
    exitButton=tk.Button(ButtonFrame,text='Exit',bg='black',fg='white'\
                         ,relief=tk.RAISED,bd=5,height=5,width=30,command=root.destroy)\
        .grid(row=0,column=10,sticky='w')
    
    mainFrame.grid(row=1,column=0)
    
    ButtonFrame.grid(row=2,column=0)
    root.mainloop()

def updateBook():
    for widgets in Canvas1.winfo_children():
        widgets.destroy()
    
    Canvas1.columnconfigure([0],weight=1,minsize=50)
    Canvas1.rowconfigure([0,1,2],weight=1,minsize=50)
    
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(headingFrame, text="Select which parameter you want to update", bg='black', fg='yellow'\
                            , font=('Courier',15),height=5,width=50)
    
    headingLabel.pack()
    headingFrame.grid(row=0,column=0)
    
    mainFrame=tk.Frame(Canvas1,bg='black',width=50)    
        
    mainFrame.columnconfigure([0,1,2],weight=1,minsize=50)
    mainFrame.rowconfigure([0,1],weight=1,minsize=30)
    
    titleButton=tk.Button(text="Update Title",master=mainFrame,bg='black',\
                          fg='white',relief=tk.RAISED,bd=5,height=5,width=30,\
                           command=lambda: option(1))
    titleButton.grid(row=0,column=0)
    
    authorButton=tk.Button(mainFrame,text='Update Author',bg='black',fg='white'\
                           ,relief=tk.RAISED,bd=5,height=5,width=30,command=lambda:option(2))
    authorButton.grid(row=1,column=0)
    
    pagesButton=tk.Button(mainFrame,text='Update Pages',bg='black',fg='white'\
                          ,relief=tk.RAISED,bd=5,height=5,width=30,command=lambda:option(3))
    
    pagesButton.grid(row=0,column=1)
    
    priceButton=tk.Button(mainFrame,text='Update Price',bg='black',fg='white'\
                          ,relief=tk.RAISED,bd=5,height=5,width=30,command=lambda:option(4))
    priceButton.grid(row=0,column=2)
    
    publisherButton=tk.Button(mainFrame,text='Update Publisher',bg='black',\
                              fg='white',relief=tk.RAISED,bd=5,height=5,width=30,\
                                  command=lambda:option(5))
    publisherButton.grid(row=1,column=1)
    
    editionButton=tk.Button(mainFrame,text='Update Edition',bg='black',fg='white'\
                            ,relief=tk.RAISED,bd=5,height=5,width=30,command=lambda:option(6))
    editionButton.grid(row=1,column=2)  
    
    button=tk.Button(Canvas1,text='Exit',bg='black',fg='white',relief=tk.RAISED,\
                     bd=5,height=5,width=30,command=root.destroy)
        
    mainFrame.grid(row=1,column=0)
    button.grid(row=2,column=0,sticky='e')


    
        