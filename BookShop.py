import json

class BookShop():

    def __init__(self):
        self.__nameF = "Book_warehouse.json"
        self.__number_of_books = len(self.read_json())

    #read_json: it returns the complete list of all books in which there are specific fields for each.
    def read_json(self) -> list:
        fileBooks = open(self.getNameJsonFile())
        dataFile = json.load(fileBooks)['Books']
        fileBooks.close()
        
        return dataFile
        
    def getNumberOfBooks(self) -> int:
        return len(self.read_json())
    
    def getNameJsonFile(self) -> str:
        return self.__nameF
    
    #check_input: method used to check that the fields entered by the user are correct and comply with the parameters for strings
    def check_input(self, title: str, author: str, ISBN: str, format: str, language: str, year: str, publishing_house: str) -> bool:
        list_compr = [title, author, ISBN, format, language, year, publishing_house]

        list_new = [isinstance(x, str) for x in list_compr if x and x.strip() != ""]

        return all(list_new)
    
    #getViewBooks: Method for displaying all book's title within the JSON file in a single view.
    def getViewBooks(self) -> None:
        
        listTitle = [x['Title'] for x in self.read_json()]

        print(f"Specifically, the titles of the books in my warehouse are as follows:: \n{', '.join(listTitle)}")


    #check_title_books: method for check if the new title book already exists. If not exists i can add a new book with this title, otherwise I won't add it
    def check_title_books(self) -> list:
        list_title = []

        for singleBook in self.read_json():
            list_title.append(singleBook['Title'].lower())
    
        return list_title
    

    #modify_book: Method for modifying a specific field in the book given the title
    def modify_book(self) -> None:
        fileOpen = open(self.getNameJsonFile())
        dataFile = json.load(fileOpen)

        bookToModify = str(input("Enter the title of the book you want to make changes to: ")) #il nome della rosa

        for x in dataFile['Books']:

            if bookToModify.lower().strip() == x['Title'].lower():
                print(f"For the title '{x['Title']}', which fields do you want to edit?? {', '.join(x.keys())}" )
                newKey = str(input("Please enter the field to be modified, respecting upper and lower case letters: "))

                if newKey == "Title":
                    print("You cannot modify the book title. Please choose another field")
                    break

                if newKey in list(x.keys()):
                    newValueForKey = str(input("Enter the value that will overwrite the original one: "))
                    x[newKey] = newValueForKey

                    if newKey == "Year":
                        if not newValueForKey.isdigit() or int(newValueForKey) < 0:
                            print("The year you entered is less than zero or you did not enter the correct digits. Please try entering a valid year!")
                            break
                    if newKey == "ISBN":
                        if not newValueForKey.isdigit() or len(newValueForKey) != 13:
                            print("The length of the ISBN code does not match the 13 digits! I can't continue!")
                            break

                    if newKey == "Format":
                        if newValueForKey in ['Papier', 'eBook']:
                            x[newKey] = newValueForKey
                        else:
                            print("I'm sorry, but I can't change this field. It can only be Papier or eBook. Always write in upper and lower case letters!")
                            break

                    print(f"After the change, this is the result {x[newKey]}")
                    
                else:
                    print("The field you entered does not respect upper and lower case letters. Please respect the characters and write the field you want to modify!")

        json_string = json.dumps(dataFile, indent = 4)
        with open(self.getNameJsonFile(), 'w') as f:
            f.write(json_string)

    #delete_book: Deletion is only possible for the shop owner, not the customer, so I ask for the master password.
    def delete_book(self) -> None:
        master_psw = str(input("Please insert the master password: ")) #MasterOfBook
        if master_psw == "MasterOfBooks":

            print("Hello MASTER, these are the titles of the books in the warehouse. Which ones do you want to permanently delete?")
            print(f"Books titles: {', '.join(self.check_title_books())}")
            delete_title = str(input("Please enter the name of the book you wish to delete: "))

            if delete_title:

                if delete_title.lower().strip() not in self.check_title_books():
                    print("The title you entered does not exist, so I will not delete any books!")
                else:
                    fileData = open(self.getNameJsonFile())
                    dataBooks = json.load(fileData)
                    listDataBooks = dataBooks.copy() #I use .copy to get a true copy

                    for book in dataBooks['Books']:
                        if book['Title'].lower() == delete_title.strip().lower():
                            titleB = book['Title']
                            listDataBooks['Books'].remove(book)
                            print(f"Book named {titleB} successfully deleted")
                    

                    jsonString = json.dumps(listDataBooks, indent = 4)
                    with open(self.getNameJsonFile(), 'w') as f:
                        f.write(jsonString)

        else:
            print("I'm sorry, but the password you entered is incorrect!")
            
    
    #add_book: method for add a new book inside the JSON
    def add_book(self, title: str, author: str, ISBN: str, format: str, language: str, year: str, publishing_house: str) -> None:

        if self.check_input(title, author, ISBN, format, language, year, publishing_house) and format.lower() in ['papier', 'ebook']:

            if title.lower() not in self.check_title_books():

                new_book = {
                    "Title": title,
                    "Author": author,
                    "ISBN": ISBN,
                    "Format": format,
                    "Language": language,
                    "Year": year,
                    "Publishing_house": publishing_house
                }

                #Read the file
                fileBooks = open(self.getNameJsonFile())
                data_file = json.load(fileBooks)
                #New book append inside the list
                data_file["Books"].append(new_book)

                #cast dict in string
                json_string = json.dumps(data_file, indent = 4, ensure_ascii = False)
                with open(self.getNameJsonFile(), 'w') as f:
                    f.write(json_string) #write the new string
                
                fileBooks.close()

                print("I add a new book! 📘")

            else:
                print(f"I'm sorry, but the book you want to add, titled {title}, already exists in our warehouse, so we cannot add a duplicate!")
        else:
            print("Sorry, but you have not entered the correct parameter(s). Remember that you must enter a string and not a blank field!")
        


    #runOperations: method used to launch the store logic, i.e. operations involving addition, modification or deletion.
    def runOperations(self) -> None:
        while True:
            answerUser = str(input("What kind of operations do you want to perform (add, modify, delete)?  If you want to exit the programme, type quit! "))
            answerUser_check = answerUser.lower().strip()

            if answerUser_check == "" or answerUser_check == "quit":
                print("Goodbye, I hope to see you again soon!")
                break
                
            #To simplify things, I assume that the books to be added are added directly without asking the user to fill in all the fields.

            if answerUser_check == "add":
                self.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Papier", "English", "1925", "Scribner")
                self.add_book("Pride and Prejudice", "Jane Austen", "9780141439518", "Papier", "English", "1813", "Penguin Classics")
                self.add_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", "Papier", "English", "1951", "Little, Brown and Company")
                self.add_book("Don Quixote", "Miguel de Cervantes", "9780060934347", "Papier", "English", "1605", "Harper Perennial Modern Classics")
                print(f"Now we have {self.getNumberOfBooks()} books in stock.")
                print("-" * 45)

            if answerUser_check == "modify":
                self.modify_book()
                print("-" * 45)

            if answerUser_check == "delete":
                self.delete_book()
                print("-" * 45)
            
            if answerUser_check not in ["add", "modify", "delete"]:
                print("To continue, I need you to choose one of three operations: add, modify or delete!")
                print("-" * 45)
            
    

        

        
    




    