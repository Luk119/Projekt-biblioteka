from Biblioteka import book_management as bm, customer_management as cm, loan_management as lm
import os

def print_menu():
    print("---Menu---")
    print("1. - Dodaj książkę")
    print("2. - Usuń książkę")
    print("3. - Zarejestruj klienta")
    print("4. - Usuń klienta")
    print("5. - Wypożycz książki")
    print("6. - Zwróć książki")
    print("0. - Zamknij program")

def main():
    while True:
        print_menu()
        choice = int(input("Wybierz opcję: "))

        if choice == 1:
            author = input("Podaj autora książki: ")
            title = input("Podaj tytuł książki: ")
            pages = input("Podaj ilość stron książki: ")
            bm.add_book(author, title, pages)
            print(f"Książka '{title}' została dodana pomyślnie")

        elif choice == 2:
            book_id_or_title = input("Podaj ID lub tytuł książki do usunięcia: ")
            bm.delete_book(book_id_or_title)

        elif choice == 3:
            print("1. Dodaj klienta")
            print("2. Zaktualizuj dane klienta")
            action = input("wybierz:")

            if action == "1":
                name = input("Podaj imię i nazwisko klienta : ")
                email = input("Podaj e-mail klienta: ")
                phone = input("Podaj numer tel. klienta:")
                cm.add_customer(name, email, phone)

            elif action == "2":
                customer_id = input("Podaj ID klienta którego chcesz zaktualizować:")
                street = input("Podaj ulicę:")
                city = input("Podaj miasto: ")
                country = input("Podaj kraj: ")
                cm.update_customer_address(customer_id, street, city, country)

            else:
                print("Wrong action")

        elif choice == 4:
            print("1. Usuń po ID")
            print("2. Usuń po imieniu")
            action = input("wybierz: ")
            if action == "1":
                customer_id = int(input("Podaj ID klienta do usunięcia: "))
                cm.remove_customer(customer_id=customer_id)
            elif action == "2":
                customer_name = input("Podaj imie klienta: ")
                cm.remove_customer(name=customer_name)
            else:
                print("Wrong action")

        elif choice == 5:
            customer_id = input("Podaj ID klienta: ")
            book_ids = input("Podaj ID książek oddzielone spacją: "). split(" ")
            lm.borrow_books(customer_id, *book_ids)

        elif choice == 6:
            customer_id = input("Podaj ID klienta:")
            book_ids = input("Podaj ID książki do oddania: ")
            lm.return_book(customer_id, *book_ids)

        elif choice == 0:
            print("Program został zakończony")
            break

        else:
            print("Zły wybór, spróbuj ponownie")

if __name__ == "__main__":
    main()