A mysql server in your local machine is required for this program to run.
My sql server description:
host="localhost"
user="jonny"
passwd="root"
database="lsm"
In mysql Workbench connect to your server under MYSQL CONNECTIONS.Then go to server tab and click users and privileges.
Click add account.On the login tab set login name as 'jonny' and password as 'root'.Authentication Type:Standard.
Then on Administrative Rules check the box of 'DBA' and then apply.

Run this query on the workbench so that the database is created.

Create database lsm;

In order to create the tables open createDB.py and run the program in a python environment.
To run the app open main.py in any ide and run it in a python environment. 
