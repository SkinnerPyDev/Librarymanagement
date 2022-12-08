#library BY nitesh
class Library():
    def __init__(self, book_list,name):
        self.book_list = book_list
        self.name = name
        self.lend_data = {}
#display all the books
    def display_books(self):
        for index,books in enumerate(self.book_list):
            print(f'({index+1}) {books}')
        print()
#lend books

    def lend_books(self,user_name,book_name):
        if book_name in self.book_list:
            if book_name not in self.lend_data.keys():
                self.lend_data.update({book_name:user_name})
                print("Now you can get the book\n")
            else:

                print(f"The book is already taken by {self.lend_data[book_name]}\n")
        else:
            print("Book is not available! First add the book\n")
                

#add books
    def add_books(self, book_name):
        self.book_list.append(book_name)
        print("Book has been added\n")


#return book
    def return_books(self,book_name):
        if book_name in self.book_list:
            if book_name in self.lend_data.keys():
                self.lend_data.pop(book_name)
                print("The book has been returned\n")
            else:
                print("The book not is lended\n")
        else:
            print("The book is not in the list\n")

def main():
    book_list = ["python","advance cpp","dsa","java"]
    name = "Nitesh"

    lib = Library(book_list,name)
    print("------------------------------")
    print(f"Welcome to {name}'s library")
    print("------------------------------")
    print("1. Display all the books")
    print("2. Lend a book")
    print("3. Add a book")
    print("4. Return a book")
    print()
    running = True
    while running:
        choice = input("Enter you choice:\n").lower()
        if choice == "1":
            lib.display_books()
        elif choice == "2":
            book_name = input("Enter the name of the book:\n").lower()
            user_name = input("Please enter you name:\n")
            lib.lend_books(user_name,book_name)
        elif choice == "3":
            book_name = input("Enter the name of the book:\n").lower()
            lib.add_books(book_name)
        elif choice == "4":
            book_name = input("Enter the name of the book:\n").lower()
            lib.return_books(book_name)
        elif choice == "q":
            running = False
         
    print("Thank you!!!")

if __name__ == "__main__":
    main()