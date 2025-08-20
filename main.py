from BookShop import BookShop

def main():

    books_obj = BookShop()
    print("Welcome to my bookshop, I am very happy to have you here. I hope it satisfies your desire to read! 🙂")
    print("First of all, I want to tell you that we currently have the following number of books in stock:", books_obj.getNumberOfBooks())
    books_obj.getViewBooks()
    print("-" * 45)

    books_obj.runOperations()

if __name__ == "__main__":
    main()