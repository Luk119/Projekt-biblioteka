
## Example 1 - modules in python
## See example in calculator folder
## Example 2 - datatime module
# from datetime import date
# print(date.today())
###########################################
## Zapis/odczyt danych typ słownik do pliku
## Example 3 - load .csv file as dictionary
# import csv
# with open('customer.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)     # each line as dict
#     for row in csv_reader:
#         print(row)

## more option, see info: https://docs.python.org/3/library/csv.html
################# Task
## Twoim zadaniem jest utworzenie pakietu obsługi
## nowych i aktualnych klientów nowo-utworzonej biblioteki
## oraz jej dostępnych zasobów. Administratorem w/w wypożyczalni
## jest biolotekarka, która świetnie zna pythona.
###############################################
############    Zasoby:
## Folder Library zawiera 3 pliki zawierające następujące dane:
## book.csv - dane książek
## address.csv - baza adresów aktualnych czytelników
## customer.csv - dane osobowe aktualnych czytelników
################################################
############  Specyfikacja oprogramowania:
## Utwórz następujące moduły:
## 1. Moduł main - główny moduł, który administruje zasobami wypożyczalni
## musi zawierać:  def __main__() ( uruchamia program)
## 2. Moduł obsługi książek zawierający 2 funkcje:
## funkcja 1: dodanie nowej książki do bazy (book.csv)
## funkcja 2: usuwanie książki do bazy opcje: wględem ID lub tytułu (book.csv)
##
## 3. Moduł obsługi klienta zawierający funkcje:
## funkcja 1: rejestracja nowego klienta lub usuwanie danych klienta z bazy
## funkcja 2: dodawanie (przez administratora) danych
## nowego klienta do bazy tj. do pliku customer.csv i address.csv
## Nowy klient podaje swoje dane (imie, nazwisko), nadawany jest w/w klientowi losowy numer ID złożony z 4 cyfr
## w folderze DATABASE tworzony jest plik tekstowy (nazwa pliku to ID klienta)
## do którego będą zapisywane dane wypożyczonej przez klienta książki oraz
## data wypożyczenia a potem zwrotu książki
## funkcja 3: usuwanie danych klienta opcje: względem ID lub NAME
## Wypożyczanie książki/-ek przez użytkownika 2 funkcje:
## funkcja 4: wypożyczenie książki lub kilku książek przez klienta
## funkcja 5: zwrot 1 książki przez klienta
##
## Jeśli skończyłeś zadanie, przyjmij rolę kolejnego programisty
## który dostał zadanie aktualizacji Twojego oprogramowania
## Nie modyfikując i nie zmieniając nazwy funkcji "udekoruj"
# funkcja nr 5: "zwrot 1 książki przez klienta" i nadpisz jej zawartość
## tak aby klient miał możliwość zwrotu dowolnej liczby książek

## WYMAGANIA:
## - możesz programować wyłącznie w paradygmacie funkcyjnym
## - utwórz funkcję wyższego rzędu
## - utwórz funkcję wielu zmiennych wejściowych
## - utwórz funkcję zagnieżdzoną
## - użyj dekoratora
## - wykonaj dokumentację dla conajmniej 1 funkcji i 1 modułu
## - conajmniej dla 2 funkcji wykonaj obsługę wyjątków  (dotyczy modułów 2-4)

## WSKAZANIA:
## - możesz zwiększyć liczbę modułów
## - dla zapisu/odczytu daty oraz danych do bazy wykorzystaj odpowiednie pakiety

