# Overview

This program is meant to edit and use exchange rates for world wide currencies. Users access the relational database to edit, update, add and delete different exchanges, along with use the information to actually convert currencies. 

Before running the program you intially need to install Python3, and download all the code. Then with the python file "currencyconverter.py" open in your prefered text editor run the code, and explore the options to edit the database and use the converter. 

I built this sofware to learn about SQL Relational Databases, as an introduction to how to use a database to solve a problem. 

[Software Demo Video](https://youtu.be/eRR4inW-A4k)

# Relational Database

For this program I am using SQLite, which is a local database, since this software is small scale, but the prinicples used here also apply to other relational databases like MySQL and MSSLQ Server.  

The strucure of the database, currency.db, is a singlular table where all exchange rates are held.

# Development Environment

This software was written with Visual Studio Code and SQLite Studio 3.3.3.

The code was developed in Python 3.10.0 with libraries:
 - SQLite3
 - Math

# Useful Websites

* [SQLite Documention ](https://www.sqlite.org/docs.html)
* [W3Schools Tutorial](https://www.w3schools.com/sql/)
* [Real Python](https://realpython.com/python-sql-libraries/#sqlite_1)
* [Python Documentation for SQLite](https://docs.python.org/3/library/sqlite3.html)

# Future Work

* Add a historical column based on past exchange rates
* Automate an update through an API
* Divide up tables into main currency to exchage rates for other currencies. 
* Loop of code so you don't have to restart the code everytime. 