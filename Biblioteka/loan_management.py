import os
import datetime
import pandas as pd
def borrow_books(customer_id, *args):
    time = datetime.date.today()
    next_month = time + datetime.timedelta(days=31)

    if os.path.exists("DATABASE"):
        df_books = pd.read_csv("Library/book.csv", usecols=["TITLE", "AUTHOR", "PAGES"])

        with open(f"DATABASE/{customer_id}.txt", "a") as file:
            for title in args:
                book = df_books[df_books["TITLE"] == title]
                author = book["AUTHOR"].values[0]
                pages = book["PAGES"].values[0]
                file.write(f"\nTITLE: {title}, AUTHOR: {author}, PAGES: {pages}, BORROWED: {time}, DUE_DATE: {next_month}, RETURNED: False")
        print("Books borrowed!")
    else:
        print("Error - Database directory does not exist")


def return_book(customer_id, book):
    time = datetime.date.today()

    if os.path.exists(f"DATABASE/{customer_id}.txt"):
        with open(f"DATABASE/{customer_id}.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 0):
            if f"TITLE: {book}" in line:
                lines[i] = lines[i].replace("False", f"{time}")

        with open(f"DATABASE/{customer_id}.txt", "w") as file:
            file.writelines(lines)
        print("Books returned successfully!")
    else:
        print("Error - Customer's file does not exist")
