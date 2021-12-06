import sqlite3
from sqlite3 import Error
import os
import random

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)



    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

# Return connection object
    return conn
# Closing connection
def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.commit()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def search(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching table")
    try:

        print("\nEnter Search Type:\n")
        print('1 -- Search By Title')
        print('2 -- Search By Category')
        print('3 -- Search By Author')
        print('4 -- Search By Publisher')
        print('5 -- Search By Language')
        print('6 -- Search By Publish Year')


        option = int(input("Option: "))
        if option == 1:
            titleSearch(_conn)
        if option == 2:
            category(_conn)
        if option == 3:
            exit()
        if option == 4:
            exit()
        if option == 5:
            exit()
        if option == 6:
            exit()

        # _conn.commit()
        # print("success")
    except Error as e:
        # # If anything goes wrong
        # _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def titleSearch(_conn):
    print("Searching By Title\n")
    try:
        book = input("Search for a book by title: ")
        sql = """SELECT b_id, b_title, a_name, c_name
                    FROM Book, Authors, Category
                    WHERE ba_id = a_id
                    AND bc_id = c_id
                    AND b_title LIKE ?"""

        cur = _conn.cursor()
        cur.execute(sql, (book + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print("The book does not exist in the database.")
            main()
        else:
            l = ("Book ID | Title | Author | Category")
            print("Displaying books found in database: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
        
        print("\nEnter 1 to learn more about book, '0' to Main Menu.")
        option = int(input("Option: "))
        if option == 1:
            bookID(_conn)
        if option == 0:
            main()
            
        # _conn.commit()
        # print("success")
    except Error as e:
        # # If anything goes wrong
        # _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def bookID(_conn):
    print("Getting Table more information...")    
    try:
        bookID = int(input("\nEnter Book ID to learn more about a book: "))
    
        sql =  """SELECT b_id, b_title, b_numPages, b_publishYear, b_language
                    FROM Book
                    WHERE b_id = ?"""

        cur = _conn.cursor()
        cur.execute(sql,(bookID, ))
        rows = cur.fetchall()

        if len(rows) == 0:
            print("Book ID not in database.")
            main()
        else:
            l = ("Book ID | Title | Number of Pages |  Publish Year |Language")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def category(_conn):
    print("All Categories")
    try:
        sql ="""SELECT distinct(c_name) as Categories
                FROM  category"""
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)

    print("Searching Table by Category")
    try:
        category = input("Search for a book by category: ")
        sql = """SELECT c_name, b_title, a_name
                    FROM Book, Category, Authors
                    WHERE bc_id = c_id
                    AND ba_id = a_id
                    AND c_name LIKE  ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (category + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print("This category does not exist in the database.")
            main()
        else:
            l = ("Category | Book Title | Author ")
            print("Displaying books of this category: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))


        # _conn.commit()
        # print("success")
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def add(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print(" add")


    while (True):
        try:
            check = input ("Enter 'Quit' to end, press 'Enter' to continue: ")
            if(check == 'Quit: '):
                main()
            userinputID = input("Enter id: ")
            userinputTitle = input("Enter Title: ")
            userinputisbn = input("Enter  isbn: ")
            userinputlangauge = input("Enter Language: ")
            userinputPageNum = input("Enter number of pages: ")
            userinputpubYear = input("Enter pub6lish year: ")
            userinputbc_id= input("Enter caregory id: ")
            userinputba_id = input("Enter author id: ")
            
            sql = """INSERT INTO Book 
                    (b_id, b_title, b_isbn, b_language, b_numPages, b_publishYear, bc_id, ba_id) 
                    VALUES ('{}','{}','{}', '{}', '{}', '{}', '{}', '{}');  """.format(userinputID,userinputTitle,userinputisbn,userinputlangauge,userinputPageNum,userinputpubYear,userinputbc_id,userinputba_id)
            cur = _conn.cursor()
            cur.execute(sql)
            _conn.commit()
            print("Book has been succesfully added.")
        except Error as e:
            # If anything goes wrong
            _conn.rollback()
            print(e)
    

def main():
    database = r"LibraryDB.sqlite"

    # create a database connection
    conn = openConnection(database)

    print("--- Library Management System ---\n")

    print('Enter number of desired option: ')
    print('1 -- Search')
    print('2 -- Add Books')
    print('3 -- View Bookmarks')
    print('4 -- Add Bookmarks')
    print('5 -- Most Popular Books')
    print('6 -- Exit')

    option = int(input('Option: '))
    with conn:
        if  option == 1:
            search(conn)
        if option == 2:
            add(conn)
        if option == 3:
           bookID(conn)
        if option == 4:
            exit()
        if option == 5:
            exit()

    # search(conn)
    # category(conn)
    closeConnection(conn, database)

if __name__ == '__main__':
    main()
