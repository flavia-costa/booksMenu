from booksMenu import *

while True:
    print("-------------------------------------")
    print("1- Create the list of books")
    print("2- Add a new book")
    print("3- Delete a book")
    print("4- List all the books")
    print("5- Exit the application")
    print("-------------------------------------")
    option = (input("Enter the desired option: "))
    print()

    if option == '1':
        print("\nYou chose option 1")
        print("Let's create the table.")
        create_table()
    elif option == '2':
        print("\nYou chose option 2")
        print("Let's add a new book.")
        insert()
    elif option == '3':
        print("\nYou chose option 3")
        print("Let's delete a book.")
        delete()
    elif option == '4':
        print("\nYou chose option 4")
        print("Let's view all the books.")
        view_all()
    elif option == '5':
        print("\nBye.")
        break
    else:
        print("\nInvalid option. Try again.")
