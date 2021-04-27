def addBook():
    book_name = input("Insert book name ->")
    author_name = input("Insert book author ->")
    #importing csv library
    import csv
    with open("booksDB.csv", mode = "w") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        writer.writerow({"BookName" : book_name,
                         "AuthorName" : author_name,
                         "SharedWith" : "None",
                         "IsRead" : False})
    print("Book was successfully added")


def listBooks():
    import csv
    with open("booksDB.csv", mode = "r") as file:
        #pasul 1 sa luam toate datele din DB
        rows = csv.DictReader(file,fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"])
        for row in rows:
            print(f"Book name is {row.get('BookName')}, auth name {row.get('AuthorName')}, is shared {row.get('ShareWith')}, is read {row.get('IsRead',False)}.")


def updateBook():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read? (Y/N)? ")
    if book_read == "Y":
        book_read = True
    else:
        book_read = False
    rows = []
    import csv
    with open("booksDB.csv", mode = "a") as file:
        rows = csv.DictReader(file,fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        for row in rows:
            if book_name == row.get("BookName"):
                row["IsRead"] = book_read
                csv_writer = csv.DictWriter(file, fieldnames=[
                    "BookName", "AuthorName", "SharedWith", "IsRead"
                ])
                csv_writer.writerow(rows)
                break

        print("Book was updated successfully!")





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