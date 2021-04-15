def addBook():
    print("Add a book option")

def listBooks():
    print("List books option")

def updateBook():
    print("Update a book option")

def shareBook():
    print("Share a book option")


# main menu for user
print("Choose an option: ")
print("1 : Add a book")
print("2 : List books")
print("3 : Update a book")
print("4 : Share a book")

option = input("Select one option -> : ")

if option == "1":
    addBook()
elif option == "2":
    listBooks()
elif option == "3":
    updateBook()
elif option == "4":
    shareBook()
else:
    print("Your option is invalid")