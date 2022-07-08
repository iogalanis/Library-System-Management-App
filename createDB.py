# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:59:25 2022

@author: galan
"""
import mysql.connector

db=mysql.connector.connect(
        host="localhost",
        user="newuser",
        passwd="root",
        database="lsm")
    
cur=db.cursor()


cur.execute("CREATE TABLE books(bid int  AUTO_INCREMENT,title char(60),\
                               Author char(30),pages int,price float,\
                                   publisher char(60),edition char(15),\
                                       status char(20),PRIMARY KEY (bid));")
cur.execute("CREATE TABLE members(mid int AUTO_INCREMENT,name char(60),class\
            char(15),address char(60),phone int,email char(60),PRIMARY KEY (mid));")

cur.execute("CREATE TABLE transactions(tid int auto_increment,bid int NOT NULL\
            ,mid int NOT NULL,doi date,dor date,fine float,PRIMARY KEY(tid),\
                FOREIGN KEY(bid) REFERENCES Books(bid),FOREIGN KEY (mid)\
                    REFERENCES members(mid));")
cur.close()

