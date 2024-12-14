# Importing Sqlite3 Module
import sqlite3
import sys
from contextlib import nullcontext
from datetime import datetime


from mimesis import Payment, Food, Person, Address, Finance, random

def main(sqlite_file: str, global_seed, person:int = -1, payment:int = -1, food:int = -1, address:int = -1, finance:int = -1):
    if global_seed is not None:
        # random.global_seed = 0xFF
        # if you supply a global_seed then you get the same results
        random.global_seed = global_seed
    db_connect = nullcontext
    try:
        # Making a connection between sqlite3 database and Python Program
        db_connect = sqlite3.connect(sqlite_file)
        # If sqlite3 makes a connection with python program then it will print "Connected to SQLite"
        # Otherwise it will show errors
        print("Beginning:")
        if int(person) > 0:
            create_person(person, "person", db_connect)
            print("-" * 80)
        if int(payment) > 0:
            create_payment(payment, "payment", db_connect)
            print("-" * 80)
        if int(food) > 0:
            create_food(food, "food", db_connect)
            print("-" * 80)
        if int(address) > 0:
            create_address(address, "address", db_connect)
            print("-" * 80)
        if int(finance) > 0:
            create_finance(finance, "finance", db_connect)
            print("-" * 80)
    except sqlite3.Error as error:
        print("Failed to connect with sqlite3 database", error)
    finally:
        # Inside Finally Block, If connection is open, we need to close it
        if db_connect:
            # using close() method, we will close the connection
            db_connect.close()
            # After closing connection object, we will print "the sqlite connection is closed"
            print("the sqlite connection is closed")

def create_person(num: int, table_name: str, db_connect: sqlite3.Connection):
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + (" (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                        "academic_degree TEXT, birthdate DATE, first_name TEXT, "
                                                        "last_name TEXT, blood_type TEXT, email TEXT, gender TEXT, "
                                                        "height REAL, language TEXT, nationality TEXT, title TEXT, phone_number TEXT)")
    db_connect.execute(sql)
    p = Person()
    sql = "INSERT INTO " + table_name + " (academic_degree, birthdate, first_name, last_name, blood_type, email, gender, height, language, nationality, title, phone_number) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"

    for i in range(num):
        t = (p.academic_degree(), p.birthdate().isoformat(), p.first_name(), p.last_name(), p.blood_type(), p.email(), p.gender(), p.height(), p.language(), p.nationality(), p.title(), p.phone_number())
        # print(t)
        db_connect.execute(sql, t)
        db_connect.commit()
        print("Person: " + str(i+1) + "/" + str(num))

def create_payment(num: int, table_name: str, db_connect: sqlite3.Connection):
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + (" (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                                        "credit_card_network TEXT, credit_card_expiration_date TEXT,"
                                                        "paypal TEXT, cvv TEXT, credit_card_number TEXT)")
    db_connect.execute(sql)
    sql = "INSERT INTO " + table_name + " (credit_card_network, credit_card_expiration_date, paypal, cvv, credit_card_number) VALUES (?, ?, ?, ?, ?)"

    p = Payment()
    for i in range(num):
        t = (p.credit_card_network(),p.credit_card_expiration_date(),p.paypal(),p.cvv(),p.credit_card_number())
        db_connect.execute(sql, t)
        db_connect.commit()
        print("Payment: " + str(i+1) + "/" + str(num))
        # print(t)
        # print("-" * 80)

def create_food(num:int, table_name: str, db_connect: sqlite3.Connection):
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + "(id INTEGER PRIMARY KEY AUTOINCREMENT, dish TEXT, drink TEXT, fruit TEXT, spices TEXT, vegetable TEXT)"
    db_connect.execute(sql)
    sql = "INSERT INTO " + table_name + " (dish,drink,fruit,spices,vegetable) VALUES (?,?,?,?,?)"

    f = Food()
    for i in range(num):
        t = (f.dish(), f.drink(), f.fruit(), f.spices(), f.vegetable())
        # print(t)
        # print("-" * 80)
        db_connect.execute(sql, t)
        db_connect.commit()
        print("Food: " + str(i+1) + "/" + str(num))

def create_address(num:int, table_name: str, db_connect: sqlite3.Connection):
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + ("(id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT,city TEXT, "
                                                        "continent TEXT, country TEXT, calling_code TEXT, postal_code TEXT, "
                                                        "province TEXT, iata_code TEXT, region TEXT, state TEXT, "
                                                        "street_name TEXT, street_number TEXT, street_suffix TEXT)")
    db_connect.execute(sql)
    sql = "INSERT INTO " + table_name + " (address,city,continent,country,calling_code,postal_code,province,iata_code,region,state,street_name,street_number,street_suffix) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

    a = Address()
    for i in range(num):
        t = (a.address(),a.city(),a.continent(),a.country(),a.calling_code(),a.postal_code(),a.province(),a.iata_code(),a.region(),a.state(),a.street_name(),a.street_number(),a.street_suffix())
        # print(t)
        # print("-" * 80)
        db_connect.execute(sql, t)
        db_connect.commit()
        print("Address: " + str(i+1) + "/" + str(num))

def create_finance(num:int, table_name: str, db_connect: sqlite3.Connection):
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + ("(id INTEGER PRIMARY KEY AUTOINCREMENT, company TEXT, bank TEXT, "
                                                        "currency_iso_code TEXT, currency_symbol TEXT, price REAL, "
                                                        "stock_exchange TEXT, stock_name TEXT, stock_ticker TEXT)")
    db_connect.execute(sql)
    sql = "INSERT INTO " + table_name + "(company,bank,currency_iso_code,currency_symbol,price,stock_exchange,stock_name,stock_ticker) VALUES (?,?,?,?,?,?,?,?)"

    f = Finance()
    for i in range(num):
        t = (f.company(), f.bank(), f.currency_iso_code(), f.currency_symbol(), f.price(), f.stock_exchange(), f.stock_name(), f.stock_ticker())
        # print(t)
        # print("-" * 80)
        db_connect.execute(sql, t)
        db_connect.commit()
        print("Finance: " + str(i+1) + "/" + str(num))


# create_person(3, "person", db_connect)
# create_payment(1, "payment", db_connect)
# create_food(1, "food", db_connect)
# create_address(1, "address", db_connect)
# create_finance(1, "finance", db_connect)

person=-1
payment=-1
food=-1
address=-1
finance=-1
global_seed = None
sqlfile = "test.db"
# random.global_seed = 0xFF
# if you supply a global_seed then you get the same results


for i in sys.argv:
    if "person" in i:
        person = int(i.replace("person=",""))
    elif "payment" in i:
        payment = int(i.replace("payment=",""))
    elif "food" in i:
        food = int(i.replace("food=",""))
    elif "address" in i:
        address = int(i.replace("address=", ""))
    elif "finance" in i:
        finance = int(i.replace("finance=", ""))
    elif "global_seed" in i:
        global_seed = i.replace("global_seed=", "")
    elif "sqlfile" in i:
        sqlfile = i.replace("sqlfile=", "")

# python main.py person=10 payment=10 food=10 address=10 finance=10 global_seed="fund"

# Getting the current date and time
dt1 = datetime.now()
print("Start Time: " + dt1.isoformat())
main(sqlfile, global_seed, person, payment, food, address, finance)
dt2 = datetime.now()
print("End Time: " + dt2.isoformat())

delta = dt2 - dt1

print("Total Time: " + str(delta))