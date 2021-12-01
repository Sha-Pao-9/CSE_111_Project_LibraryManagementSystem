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


def search(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Searching table")
    try:
        book = input("Search for a book by title: ")
        sql = """SELECT b_title, r_rating, a_name, b_publishYear, b_numPages
                    FROM Book, Ratings, Authors
                    WHERE b_id = r_id
                    AND ba_id = a_id
                    AND b_title = ?"""

        cur = _conn.cursor()
        cur.execute(sql, (book,))
        rows = cur.fetchall()

        if len(rows) == 0:
            print("The book does not exist in the database.")
            main()
        else:
            l = ("Title | Rating | Author | Publish Year | Number of Pages")
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

    print("Hello, this works! Enter 1 to search by book title: ")
    answer = input()
    with conn:
        if answer == 1:
            search(conn)
        if answer == 2:
            exit()   


    closeConnection(conn, database)
    search(conn)

if __name__ == '__main__':
    main()
