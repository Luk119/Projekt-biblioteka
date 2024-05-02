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
            name = input("Podaj imię klienta: ")
            surname = input("Podaj nazwisko klienta: ")
            customer_id = cm.register_customer(name, surname)
            print(f"Klient został zarejestrowany, jego ID to: {customer_id}")

        elif choice == 4:
            customer_id = input("Podaj ID klienta do usunięcia: ")
            cm.remove_customer_by_id(customer_id)
            print("Klient został usunięty")

        elif choice == 5:
            customer_id == input("Podaj ID klienta: ")
            book_ids = input("Podaj ID książek oddzielone spacją: "). split(" ")
            lm.borrow_books(customer_id, *book_ids)
            print("Książki zostąły wypożycznone")

        elif choice == 6:
            customer_id = input("Podaj ID klienta:")
            book_ids = input("Podaj ID książek oddzielone spacją: ").split()
            lm.return_books(customer_id, *book_ids)
            print("Książki zostały zwrócone")

        elif choice == 0:
            print("Program został zakończony")
            break

        else:
            print("Zły wybór, spróbuj ponownie")

if __name__ == "__main__":
    main()