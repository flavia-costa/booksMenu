import sqlite3

def create_table():
    db = sqlite3.connect('books.db')
    try:
        cur = db.cursor()
        sql_command = '''CREATE table books
                            (bookName text (50) primary key,
                            author text (30) not null);'''
        cur.execute(sql_command)
        print ('Livros table created successfully')
    except sqlite3.Error as error:
        print("Error occurred:", error)
        db.rollback()
    db.close()

def insert():
    db = sqlite3.connect('books.db')
    sql_command = '''insert into books
                    (bookName, author) values(?,?);'''
    name_input = input("Enter book name: ")
    author_input = input("Enter author's name: ")
    try:
        cur = db.cursor()
        cur.execute(sql_command, (name_input, author_input))
        db.commit()
        print ("Book added successfully")
    except sqlite3.Error as error:
        print("Error occurred:", error)
        db.rollback()
    db.close()

def delete():
    db = sqlite3.connect('books.db')
    name_input = input("Enter the name of the book to be deleted: ")
    cur = db.cursor()
    sql_command="SELECT bookName, author FROM books where bookName=?;"
    cur.execute(sql_command, (name_input,))
    rows = cur.fetchall()
    for row in rows:
        print("This is the book that will be deleted:", row)
        sql_command = "DELETE FROM books where bookName=?;"
    try:
        cur = db.cursor()
        cur.execute(sql_command, (name_input,))
        db.commit()
        print("Book deleted successfully")
    except sqlite3.Error as error:
        print("Error occurred:", error)
        db.rollback()
    db.close()

def view_all():
    db=sqlite3.connect('books.db')
    cur=db.cursor()
    sql_command="SELECT bookName, author FROM books;"
    cur.execute(sql_command)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
