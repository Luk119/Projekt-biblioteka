from Biblioteka import book_management as bm, customer_management as cm, loan_management as lm, is_valid as iv

def print_menu():
    print("---Menu---")
    print("1. - Add a book")
    print("2. - Delete the book")
    print("3. - Register a customer")
    print("4. - Delete the customer")
    print("5. - Borrow books")
    print("6. - Return books")
    print("7. - Show a list of books")
    print("8. - Show a list of customers")
    print("0. - Close the program")


def main():
    while True:
        print_menu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            title = input("Type the book title: ")
            author = input("Type the book author: ")
            pages = input("Type the book pages: ")
            bm.add_book(author, title, pages)

        elif choice == 2:
            book_id_or_title = input("Type the book id or title to be deleted: ")
            bm.delete_book(book_id_or_title)

        elif choice == 3:
            print("1. Add a customer")
            print("2. Update user address")
            action = input("Choose:")

            if action == "1":
                name = input("Type the client name : ")
                email = input("Type the client e-mail: ")
                phone = input("Type the client phone number: ")
                cm.add_customer(name, email, phone)

            elif action == "2":
                customer_id = int(input("Type the client ID that you want to update: "))
                street = input("Type the street address: ")
                city = input("Type the city address: ")
                country = input("Type the country: ")
                cm.update_customer_address(customer_id, street, city, country)

            else:
                print("Wrong action")

        elif choice == 4:
            print("1. Delete by ID")
            print("2. Delete by name")
            action = input("Choose: ")

            if action == "1":
                customer_id = int(input("Type the client ID that you want to delete: "))
                cm.remove_customer(customer_id=customer_id)
            elif action == "2":
                customer_name = input("Type the client name that you want to delete: ")
                cm.remove_customer(name=customer_name)
            else:
                print("Wrong action")

        elif choice == 5:
            customer_id = int(input("Type the client ID: "))
            if iv.is_updated(customer_id):
                book_ids = input("Type the titles of the books that you want to borrow (by comma - ', '): "). split(", ")
                lm.borrow_books(int(customer_id), *book_ids)
            else:
                print("This customer is not updated yet. Complete the address information.")

        elif choice == 6:
            customer_id = input("Type the client ID: ")
            book_titles = input("Type the titles of the books that you want to return (by comma - ', '): "). split(", ")
            lm.return_book(int(customer_id), *book_titles)

        elif choice == 7:
            print("List of books:")
            bm.print_books()

        elif choice == 8:
            print("List of customers:")
            cm.print_customers()

        elif choice == 0:
            print("The program has ended")
            break

        else:
            print("Wrong choice, try again")


if __name__ == "__main__":
    main()