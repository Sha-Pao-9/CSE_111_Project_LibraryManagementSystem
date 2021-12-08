import sqlite3
from sqlite3 import Error
import os
import random
from colorama import init, Fore, Back, Style
from termcolor import colored


def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
    except Error as e:
        print(e)


# Return connection object
    return conn
# Closing connection
def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.commit()
    except Error as e:
        print(e)


def Viewbookmarks(_conn,user):
    print("++++++++++++++++++++++++++++++++++")
    print(Fore.GREEN + user + " Bookmarks")
    print(Style.RESET_ALL)
    try:
        sql = """
        SELECT  b_id, bm_title, a_name, c_name
        FROM    User,
                Bookmarks,
                Book,
                Category,
                Authors 
        WHERE   u_userkey = bm_userkey
        AND     bm_title = b_title
        AND     ba_id = a_id
        AND     bc_id = c_id
        AND     u_name = '{}'""".format(user)

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.RED + "No Bookmarks Found For User: " + user)
            print(Style.RESET_ALL)

            print(Fore.BLUE + "Want to add to your bookmarks? Enter '1'. Enter '0' for Main Menu")
            print(Style.RESET_ALL)

            option = int(input("Option: "))
            if option == 1:
                listBooks(_conn)
                addBookmarks(_conn, user)
            if option == 0:
                main()
        else:
            l = ("Category | Book Title | Author ")
            print("Displaying books of this category: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
    
    except Error as e:
        # # If anything goes wrong
        # _conn.rollback()
        print(e)

def listBooks(_conn):
    print("++++++++++++++++++++++++++++++++++")
    try:
        print("List of current books: ")
        sql = """SELECT b_id, b_title
                    FROM Book;"""

        cur = _conn.cursor()
        cur.execute(sql, )
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def search(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching table")
    try:

        print("\nEnter Search Type:\n")
        print('0 -- Go Back to Menu')
        print('1 -- Search By Title')
        print('2 -- Search By Category')
        print('3 -- Search By Author')
        print('4 -- Search By Publisher')
        print('5 -- Search By Language')
        print('6 -- Search By Publish Year')


        option = int(input("Option: "))
        if option == 0:
            main()
        if option == 1:
            titleSearch(_conn)
        if option == 2:
            category(_conn)
        if option == 3:
            authorSearch(_conn)
        if option == 4:
            publisherSearch(_conn)
        if option == 5:
            languageSearch(_conn)
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
                    FROM Book, Authors, Category,BookAuthor
                    WHERE BAa_id = a_id
                    AND BAb_id = b_id
                    AND bc_id = c_id
                    AND b_title LIKE ?"""

        cur = _conn.cursor()
        cur.execute(sql, (book + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.RED + "The book does not exist in the database.")
            print(Style.RESET_ALL)
            print(Fore.BLUE + "Want to add book to database? Enter '1'. Enter '2' to search again. Enter '0' for Main Menu")
            print(Style.RESET_ALL)

            option = int(input("Option: "))
            if option == 1:
                addBook(_conn)
            if option == 0:
                main()
            if option == 2:
                titleSearch(_conn)

        else:
            l = ("Book ID | Title | Author | Category")
            print("Displaying books found in database: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
        
        print(Fore.BLUE + "\nEnter 1 to learn more about book, '0' to Main Menu.")
        print(Style.RESET_ALL)
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
        sql = """SELECT b_id, c_name, b_title, a_name
                    FROM Book, Category, Authors
                    WHERE bc_id = c_id
                    AND ba_id = a_id
                    AND c_name LIKE  ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (category + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.RED + "This category does not exist in the database.")
            print(Style.RESET_ALL)
            main()
        else:
            l = ("Book ID | Category | Book Title | Author ")
            print("Displaying books of this category: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
                
        print(Fore.BLUE + "\nEnter 1 to learn more about book, '0' to Main Menu.")
        print(Style.RESET_ALL)
        option = int(input("Option: "))
        if option == 1:
            bookID(_conn)
        if option == 0:
            main()

        # _conn.commit()
        # print("success")
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def authorSearch(_conn):
    print("All Authors")
    try:
        sql ="""SELECT distinct(a_name) as Author
                FROM  Authors"""
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)

    print("Searching Table by Author")
    try:
        author = input("Search for a book by author: ")
        sql = """SELECT b_id, a_name, b_title, c_name
                    FROM Book, Category, Authors
                    WHERE bc_id = c_id
                    AND ba_id = a_id
                    AND a_name LIKE  ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (author + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.RED + "This author does not exist in the database.")
            print(Style.RESET_ALL)
            main()
        else:
            l = ("Book ID | Author | Book Title | Category ")
            print("Displaying books of this author: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
                
        print(Fore.BLUE + "\nEnter 1 to learn more about book, '0' to Main Menu.")
        print(Style.RESET_ALL)
        option = int(input("Option: "))
        if option == 1:
            bookID(_conn)
        if option == 0:
            main()

        # _conn.commit()
        # print("success")
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def publisherSearch(_conn):
    print("All Publishers")
    try:
        sql ="""SELECT distinct(p_name) as Publishers
                FROM  Publisher"""
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)

    print("Searching Table by Publisher")
    try:
        publisher = input("Search for a book by publisher: ")
        sql = """SELECT b_id, b_title, p_name
                    FROM Book, Publisher, PublisherAuthors
                    WHERE p_id = PAp_id
                    AND ba_id = PAa_id
                    AND p_name LIKE  ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (publisher + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.RED + "This publisher does not exist in the database.")
            print(Style.RESET_ALL)
            main()
        else:
            l = ("Book ID | Book Title | Publisher ")
            print("Displaying books of this publisher: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
                
        print(Fore.BLUE + "\nEnter 1 to learn more about book, '0' to Main Menu.")
        print(Style.RESET_ALL)
        option = int(input("Option: "))
        if option == 1:
            bookID(_conn)
        if option == 0:
            main()

        # _conn.commit()
        # print("success")
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def languageSearch(_conn):
    print("All Languages")
    try:
        sql ="""SELECT distinct(b_language) as Languages
                FROM  Book"""
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        _conn.rollback()
        print(e)

    print("Searching Table by Language")
    try:
        language = input("Search for a book by language: ")
        sql = """SELECT b_id, b_title, b_language
                    FROM Book
                    WHERE b_language LIKE  ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (language + '%',))
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.RED + "This language does not exist in the database.")
            print(Style.RESET_ALL)
            main()
        else:
            l = ("Book ID | Book Title | Language ")
            print("Displaying books of this language: \n")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))
                
        print(Fore.BLUE + "\nEnter 1 to learn more about book, '0' to Main Menu.")
        print(Style.RESET_ALL)
        option = int(input("Option: "))
        if option == 1:
            bookID(_conn)
        if option == 0:
            main()

        # _conn.commit()
        # print("success")
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
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
            print(Fore.RED + "Book ID not in database.")
            print(Style.RESET_ALL)
            main()
        else:
            l = ("Book ID | Title | Number of Pages |  Publish Year |Language")
            print(l)
            for row in rows:
                print('|'.join([str(r) for r in row]))

        print(Fore.BLUE + "\nWant to search again?, Enter '1'. Enter '0' for Main Menu.")
        print(Style.RESET_ALL)
        option = int(input("Option: "))
        if option == 1:
            search(_conn)
        if option == 0:
            main()

    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def addBook(_conn):
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
            userinputpubYear = input("Enter publish year: ")
            userinputbc_id= input("Enter caregory id: ")
            userinputba_id = input("Enter author id: ")
            
            sql = """INSERT INTO Book 
                    (b_id, b_title, b_isbn, b_language, b_numPages, b_publishYear, bc_id, ba_id) 
                    VALUES ('{}','{}','{}', '{}', '{}', '{}', '{}', '{}');  """.format(userinputID,userinputTitle,userinputisbn,userinputlangauge,userinputPageNum,userinputpubYear,userinputbc_id,userinputba_id)
            cur = _conn.cursor()
            cur.execute(sql)
            _conn.commit()
            print(Fore.GREEN + "Book has been succesfully added.")
            print(Style.RESET_ALL)
        except Error as e:
            # If anything goes wrong
            _conn.rollback()
            print(e)

def createUser(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print(" add")

    try:
        check = input ("Enter 'Quit' to end, press 'Enter' to continue: ")
        if(check == 'Quit: '):
            main()
        userinputID = input("Enter id: ")
        userinputName = input("Enter name: ")
        userinputEmail = input("Enter email: ")
        userinputPassword = input("Enter password: ")

        sql = """INSERT INTO User 
                (u_userkey, u_name, u_email, u_password) 
                VALUES ('{}','{}','{}', '{}');  """.format(userinputID, userinputName,userinputEmail,userinputPassword)
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
        print(Fore.GREEN + "User has been succesfully created.")
        print(Style.RESET_ALL)
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)
    
def checkUser(_conn):
    print("++++++++++++++++++++++++++++++++++")

    print("Searching Table by User")
    try:
        user = input("Enter Username: ")
        password = input("Enter password: ")
        sql = """SELECT u_userkey, u_name
                    FROM User
                    WHERE u_name = ?
                    AND u_password = ?;"""

        cur = _conn.cursor()
        cur.execute(sql, (user, password,))
        rows = cur.fetchall()

        if len(rows) == 0:
            print(Fore.YELLOW + "This user does not exist, or invalid credentials. ")
            print(Style.RESET_ALL)
            print("\nCreate new user? Enter '1'. Try again? Enter '2'. For Main Menu, enter '0'")
            option = int(input("Option: "))
            if option == 0:
                main()
            if option == 1:
                createUser(_conn)
            if option == 2:
                checkUser(_conn)
        else:
            print("Displaying User Bookmarks: \n")
            Viewbookmarks(_conn,user)
            print(Fore.BLUE + "Add More bookmarks? Enter '1', '0' for Main Menu")
            print(Style.RESET_ALL)
            option = int(input("Option: "))
            if option == 0:
                main()
            if option == 1:
                addBookmarks(_conn, user)

        _conn.commit()
        print("success")
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

def addBookmarks(_conn, user):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching Table by User")

    try:
        userinputID = int(input("Enter id: "))


        sql = """INSERT INTO Bookmarks 
                    SELECT b_id, u_userkey, b_title, a_name, p_name, b_numPages, b_publishYear
                    FROM Book, Bookmarks, User, Authors, Publisher, PublisherAuthors
                    WHERE b_id = bm_id
                    AND bm_userkey = u_userkey
                    AND ba_id = a_id
                    AND p_id = PAp_id
                    AND ba_id = PAa_id
                    AND u_name = ?
                    AND b_id = ?; """
        cur = _conn.cursor()
        cur.execute(sql, (user, userinputID, ))
        _conn.commit()
        print(Fore.GREEN + "Your bookmark has been succesfully added!")
        print(Style.RESET_ALL)
        Viewbookmarks(_conn, user)
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)

def deleteBook(_conn):
    print("Delete Books")
    try:
        bookID = int(input("\nEnter Book ID to delete book: "))
    
        sql =  """DELETE FROM Book
                     WHERE b_id = ?;"""

        cur = _conn.cursor()
        cur.execute(sql,(bookID, ))
        _conn.commit()

        print(Fore.GREEN + "Book has been succesfully deleted.")
        print(Style.RESET_ALL)
        main()
    except Error as e:
        # If anything goes wrong
        _conn.rollback()
        print(e)
    
def main():
    database = r"LibraryDB.sqlite"

    # create a database connection
    conn = openConnection(database)

    print(Fore.BLUE + "--- Library Management System ---\n")
    print(Style.RESET_ALL)

    print(Fore.GREEN + 'Enter number of desired option: ')
    print(Style.RESET_ALL)

    print('1 -- Search')
    print('2 -- Add Books')
    print('3 -- View Bookmarks')
    print('4 -- Add Bookmarks')
    print('5 -- Delete Books')
    print('6 -- Exit')

    option = int(input('Option: '))
    with conn:
        if  option ==0:
            createUser(conn)
        if  option == 1:
            search(conn)
        if option == 2:
            addBook(conn)
        if option == 3:
           checkUser(conn)
        if option == 4:
            addBookmarks(conn)
        if option == 5:
            deleteBook(conn)
        if option == 6:
            exit()
            
    closeConnection(conn, database)

if __name__ == '__main__':
    main()