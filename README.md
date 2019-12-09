# datarep-project
HDip Data Analytics 2019 Data Representation project   

**Purpose**  
Demonstrate a python Flask server with a REST API that performs CRUD operations on two sql tables, and an   
html web interface that uses AJAX to connect to the server to perform the CRUD operations. The 'MySQL' package   
is used to access and update the sql database.

**Repository files**  
1. server.py      - the Flask server to perform the CRUD operations  
2. projectDAO.py  - library file loaded by 'server.py', to execute the sql operations   
3. createdb.py    - code to create the database ('datarepresentation') if it doesn't exist  
                 create 2 tables ('cds' and 'dvds') if they don't exist  
                 load a few sample records into each table  
4. dbconfig.py    - config file with the 'MySQL' params to connect to the database. Used by 'createdb' and 'projectDAO'  
5. DRproject.html - the web interface that issues AJAX commands to 'server' to read/update the sql tables

**To run**  
'MySQL' will need to be installed first (if it is not already present). For instructions:  
https://dev.mysql.com/doc/mysql-installation-excerpt/5.5/en/windows-install-archive.html
Download and include python option.  

At the command prompt:
If 'flask' and 'mysql-connector' are not yet installed:  
*pip install flask*  
*pip install mysql-connector*

*python createdb.py*     - this code uses 'MySQL' to create a database 'datarepresentation'and two sql tables 'cds' and 
                         'dvds', and writes 3 samples records into each. A temporary record is also first inserted into each 
                         and then deleted. This is because if a record with index 1 is present in 'dvds' that is subsequently
                         updated using the application, the records for both tables are incorrectly displayed - I could not fix this, 
                         other than by deleting the record with index 1 - this error then no longer occurs.

*set FLASK-APP server*   - 'server' is the name of the server here. 
*flask run*              - this starts the server running at 127.0.0.1:5000

In a browser address bar:
*http://127.0.0.1:5000/DRproject.html*   - starts the web interface that uses AJAX to perform database I/O via the server
                                         CRUD operations can then be performed against both tables.
                                         
**Table format**  
*'cds'*  
id       int     NOT NULL AUTO-INCREMENT    - integer key used by 'MySQL' for table operations  
album    text    VARCHAR(255)               - album name, up to 255 characters, eg 'Secret People'  
artist   text    VARCHAR(255)               - artist/band name, up to 255 characters, eg 'Tim Edey'     
price    int     Int                        - CD price as a simple integer, eg 1000  (for €10.00)  
   
*'dvds'*  
id       int     NOT NULL AUTO-INCREMENT    - integer key used by 'MySQL' for table operations  
title    text    VARCHAR(255)               - film name, up to 255 characters, eg 'Schindlers List'  
director text    VARCHAR(255)               - artist/band name, up to 255 characters, eg 'Steven Spielberg'     
price    int     Int                        - CD price as a simple integer, eg 899  (for €8.99)     
   
**Log file**  
'server' creates a log file *'log.log'*, listing errors and received commands
