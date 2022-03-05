# Import module to access SQLite db
import sqlite3

# Import module for math rounding
import math

# function to retrieve exchange rate from SQL database by passing in both currency types
def getExchange(currency1, currency2):

    # create a list to hold the exchange infomation when we pull it from database
    Info = []

    # creating a connection to database
    con = sqlite3.connect("currency.db")
    cur = con.cursor()

    # Opening connection to database
    var = (
        "SELECT * FROM exchange WHERE first_country = '"
        + currency1
        + "' AND second_country = '"
        + currency2
        + "'"
    )
    for row in cur.execute(var):
        Info.append(row)
    return Info[0]


# function to convert to new currency by passing in oldAmount and exchange rate
def convert(oldAmount, exchangeRate):

    # Mulitply old amount with exchange rate from database to get new amount
    newAmount = oldAmount * float(exchangeRate)

    # return rounded currency in new type
    return newAmount


# function to prompt user for what they want to exchange
def exchangeCurrency():
    # PROMPT for currency currency type
    currency1 = input(
        "What is the current currency type? (ex. USD, MXN, EUR, JPY) "
    )

    # PROMPT for new currency type
    currency2 = input(
        "What is the desired currency type? (ex. USD, MXN, EUR, JPY) "
    )

    # PROMPT for currency amount
    oldAmount = float(
        input(
            "How much money do you have in the current currency? (ex. 13.98) "
        )
    )

    # Call getExchange to retrieve exchange rate information
    exchangeinfo = getExchange(currency1, currency2)
    exchangeRate = exchangeinfo[2]

    # Call convert to get currency amount in new type
    newAmount = convert(oldAmount, exchangeRate)

    # Round to the nearest tenth
    ConvertedResult = round(newAmount, 2)

    # PUT result for user
    print(ConvertedResult)


# function to update a row in the database
def updateDatabase():

    # create a lists for later use
    Info = []
    Info2 = []

    # creating a connection to database
    con = sqlite3.connect("currency.db")
    cur = con.cursor()

    print("What conversion would you like to update?")

    # print datatable so it can be edited
    var = "SELECT * FROM exchange"
    for row in cur.execute(var):
        print(row)

    # prompt for infomation to update
    country1 = input(
        "What is first column country on the row that would you like to update? "
    )
    country2 = input(
        "What is second column country on the row that would you like to update? "
    )
    newrate = input(
        "what is the new rate for these countries? (decimal please) "
    )

    # update information as requested
    var3 = (
        "UPDATE exchange SET rate = "
        + newrate
        + " WHERE first_country = '"
        + country1
        + "' AND second_country = '"
        + country2
        + "'"
    )
    con.execute(var3)
    con.commit()

    # Select updated row for printing
    var2 = (
        "SELECT * FROM exchange WHERE first_country = '"
        + country1
        + "' AND second_country = '"
        + country2
        + "'"
    )

    for row2 in cur.execute(var2):
        Info2.append(row2)

    # Print results0
    print("You have updated that entry to be :")
    print(Info2[0])


# function to add a row in the database
def addtoDatabase():

    # create a list to hold the exchange infomation when we pull it from database
    Info = []

    # creating a connection to database
    con = sqlite3.connect("currency.db")
    cur = con.cursor()

    print("What conversion would you like to add?")

    # print datatable so it can be edited
    var = "SELECT * FROM exchange"
    rows = con.execute(var)
    for row in cur.execute(var):
        print(row)

    # prompt for infomation to add
    country1 = input(
        "What is first column country/currency on the row that would you like to add? (ex. USD) "
    )
    country2 = input(
        "What is second column country/currency on the row that would you like to add? (ex. JPY) "
    )
    rate = input("what is the rate for these countries? (decimal please) ")

    # execute addition
    var = (
        "INSERT INTO exchange(first_country, second_country, rate) VALUES ( '"
        + country1
        + "', '"
        + country2
        + "', '"
        + rate
        + "')"
    )
    cur.execute(var)
    con.commit()
    print("You have add an entry: ")

    # Select updated row for printing
    var2 = (
        "SELECT * FROM exchange WHERE first_country = '"
        + country1
        + "' AND second_country = '"
        + country2
        + "'"
    )
    rows = con.execute(var2)

    # Print Results
    for row in cur.execute(var2):
        print(row)


# function to delete a row in the database
def deletefromDatabase():

    # creating a connection to database
    con = sqlite3.connect("currency.db")
    cur = con.cursor()

    Info = []

    print("What conversion would you like to delete?")

    # print datatable so it can be edited
    var = "SELECT * FROM exchange"
    rows = con.execute(var)
    for row in cur.execute(var):
        print(row)

    # prompt for infomation to delete
    country1 = input(
        "What is first column country/currency on the row that would you like to delete? "
    )
    country2 = input(
        "What is second column country/currency on the row that would you like to delete? "
    )

    # execute deletion
    var = (
        "DELETE FROM exchange WHERE first_country = '"
        + country1
        + "' AND second_country = '"
        + country2
        + "'"
    )

    con.execute(var)
    con.commit()
    print("Success!")


# run of code
choice = input(
    "What would you like to do? \n A) update database \n B) add to database \n C) convert currency \n D) delete from database \n"
)

if choice == "C":
    exchangeCurrency()
elif choice == "A":
    updateDatabase()
elif choice == "B":
    addtoDatabase()
elif choice == "D":
    deletefromDatabase()
