# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 23:29:36 2021

@author: galan
"""
import os
import mysql.connector
import tkinter as tk
from tkinter import messagebox


#Register the book to the database
def bookReg():
    db=mysql.connector.connect(
        host="localhost",
        user="jonny",
        passwd="root",
        database="lsm")
    
    cur=db.cursor()
    
    if(len(bookTitle.get())==0 or len(bookAuthor.get())==0 or len(bookPublisher.get())==0\
           or len(bookPages.get())==0 or len(bookPrice.get())==0 or len(bookEdition.get())==0\
               or len(bookCopies.get())==0):
       messagebox.showinfo("Please fill all the required parameters")
    else:
    
        title = bookTitle.get()
        author = bookAuthor.get()
        publisher = bookPublisher.get()
        pages = bookPages.get()
        price=bookPrice.get()
        edition=bookEdition.get()
        copies= int(bookCopies.get())
    

        insertBooks='insert into books(title,Author,pages,price,publisher,edition,status)\
            values(%s,%s,%s,%s,%s,%s,%s)';
            
        values=(title,author,pages,price,publisher,edition,"available")
        
        for i in range(0,copies):
        
            try:
                cur.execute(insertBooks,values)
                db.commit()
                messagebox.showinfo('Success',"Book added successfully")
            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)
                messagebox.showinfo(err)
    cur.close() 
            
def addBook():
    global bookID,bookTitle,bookAuthor,bookPublisher,bookPages,bookPrice,\
 bookEdition,bookCopies

    root = tk.Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1000x1000")
    
    
    Canvas1 = tk.Canvas(root,width=1000,height=1000,bg="#ff6e40")

    Canvas1.pack(expand=True,fill=tk.BOTH)
    
    headingFrame=tk.Frame(Canvas1,bg='Black',bd=5)
    headingLabel = tk.Label(Canvas1, text="Add Books", bg='black', fg='yellow'\
                            , font=('Courier',15),height=5,width=30)
    
    headingLabel.pack()
    headingFrame.pack()
    
    mainFrame=tk.Frame(Canvas1,bg='black',width=50)
    
    mainFrame.columnconfigure([0,1],weight=1,minsize=50)
    mainFrame.rowconfigure([0,1,2,3,4,5,6,7],weight=1,minsize=50)
    
        
    #BOOK TITLE
    bookTitleLabel=tk.Label(mainFrame,text='Book Title: ',bg='black',\
                            fg='white',height=2,width=14)
    bookTitleLabel.grid(row=1,column=0)
        
    bookTitle=tk.Entry(mainFrame,width=50)
    bookTitle.grid(row=1,column=1)
    
    #BOOK AUTHOR
    bookAuthorLabel=tk.Label(mainFrame,text='Book Author: ',bg='black',\
                             fg='white',height=2,width=14)
    bookAuthorLabel.grid(row=2,column=0)
    bookAuthor=tk.Entry(mainFrame,width=50)
    bookAuthor.grid(row=2,column=1)
    
    #BOOK PUBLISHER
    bookPublisherLabel=tk.Label(mainFrame,text='Book Publisher: ',bg='black',\
                                fg='white',height=2,width=14).grid(row=3,column=0)
    bookPublisher=tk.Entry(mainFrame,width=50)
    bookPublisher.grid(row=3,column=1)
    
    #BOOK PAGES
    bookPagesLabel=tk.Label(mainFrame,text='Book Pages: ',bg='black',\
                            fg='white',height=2,width=14).grid(row=4,column=0)
    bookPages=tk.Entry(mainFrame,width=50)
    bookPages.grid(row=4,column=1)
    
    #BOOK PRICE
    bookPriceLabel=tk.Label(mainFrame,text='Book Price: ',bg='black',\
                            fg='white',height=2,width=14).grid(row=5,column=0)
    bookPrice=tk.Entry(mainFrame,width=50)
    bookPrice.grid(row=5,column=1)
    
    #BOOK EDITION
    bookEditionLabel=tk.Label(mainFrame,text='Book Edition: ',bg='black',\
                              fg='white',height=2,width=14).grid(row=6,column=0)
    bookEdition=tk.Entry(mainFrame,width=50)
    bookEdition.grid(row=6,column=1)
    
    #BOOK COPIES 
    
    bookCopiesLabel=tk.Label(mainFrame,text='Book copies: ',bg='black',\
                             fg='white',height=2,width=14).grid(row=7,column=0)
    bookCopies=tk.Entry(mainFrame,width=50)
    bookCopies.grid(row=7,column=1)
    
    ButtonFrame=tk.Frame(Canvas1,bg="#ff6e40")
    ButtonFrame.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11],weight=1,minsize=50)
    ButtonFrame.rowconfigure([0],weight=1,minsize=50)
    
    submitButton=tk.Button(ButtonFrame,text='Submit',bg='black',fg='white'\
                           ,relief=tk.RAISED,bd=5,height=5,width=30,command=bookReg)\
        .grid(row=0,column=2)
        
    exitButton=tk.Button(ButtonFrame,text='Exit',bg='black',fg='white'\
                         ,relief=tk.RAISED,bd=5,height=5,width=30,command=root.destroy)\
        .grid(row=0,column=10)
    
    mainFrame.pack()
    
    ButtonFrame.pack(side=tk.LEFT)
    
    root.mainloop()


    
    
        
    
    