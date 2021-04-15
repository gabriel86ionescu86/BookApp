def addBook():
    book_name = input("Insert book name ->")
    author_name = input("Insert book author ->")
    #importing csv library
    import csv
    with open("booksDB.csv", "w") as file:
        writer = csv.DictWriter(file,fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        writer.writerow({"BookName" : book_name,
                         "AuthorName" : author_name})

    print("Book was successfully added")









def listBooks():
    print("List books option")

def updateBook():
    print("Update a book option")

def shareBook():
    print("Share a book option")


# main menu for user
print("Menu options: ")
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