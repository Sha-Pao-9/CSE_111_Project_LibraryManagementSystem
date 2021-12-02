import sqlite3
from sqlite3 import Error
import os
import random

# DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'LibraryDB.sqlite')

# conn = sqlite3.connect('LibraryDB.sqlite')

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

def add(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print(" add")


    while (True):
        try:
            check = input ("Enter 'Quit' to end")
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
        except Error as e:
            # If anything goes wrong
            _conn.rollback()
            print(e)


def search(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching table")
    try:
        book = input("Search for a book by title: ")
        sql = """SELECT b_id, b_title, a_name, c_name
                    FROM Book, Authors, Category
                    WHERE ba_id = a_id
                    AND bc_id = c_id
                    AND b_title = ?"""

        cur = _conn.cursor()
        cur.execute(sql, (book,))
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
            
        bookID = int(input("\nEnter Book ID to learn more about a book, '0' to exit: "))
        
        if bookID != 0:
            sql =  """SELECT b_id, b_title, b_numPages, b_publishYear, p_name, b_language
                        FROM Book, Authors, Publisher, PublisherAuthors, Ratings
                        WHERE ba_id = a_id
                        AND p_id = PAp_id
                        AND r_id = b_id
                        AND b_id = ?"""

            cur = _conn.cursor()
            cur.execute(sql, (book, bookID, ))
            rows = cur.fetchall()

            if len(rows) == 0:
                print("The book ID does not exist in the database.")
                main()

            else:
                l = ("Book ID | Title | Number of Pages |  Publish Year | Publisher | Language")
                print("Displaying books found in database: \n")
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

def displayCat(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("All Categories")
    try:
        sql ="""SELECT distinct(c_name) as Categories
                FROM   category"""
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)

def displayAuth(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("All Authors")
    try:
        sql ="""SELECT distinct(a_name) 
                FROM   Authors"""
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)


def category(_conn):
    print("++++++++++++++++++++++++++++++++++")
    #print("Searching Table by Category")
    try:
        category = input("Search for a book by category: ")
        sql = """SELECT c_name, b_title, a_name
                    FROM Book, Category, Authors
                    WHERE bc_id = c_id
                    AND ba_id = a_id
                    AND c_name = ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (category,))
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


def main():
    database = r"LibraryDB.sqlite"

    # create a database connection
    conn = openConnection(database)

    print("--- Library Management System ---\n")
    print('Enter number of desired option: ')
    print('1 -- Search By Title')
    print('2 -- Search By Category')
    print('3 -- Search By Ratings')
    print('4 -- Create New Account')
    print('5 -- Exit')
    print('6 -- add book')

    option = int(input('Option: '))
    with conn:
        if  option == 1:
            search(conn)
        if option == 2:
            displayCat(conn)
            category(conn)
            exit()
        if option == 3:
            exit()
        if option == 4:
            exit()
        if option == 5:
            exit()
        if option == 6:
            add(conn)

    # search(conn)
    # category(conn)
    closeConnection(conn, database)

if __name__ == '__main__':
    main()
