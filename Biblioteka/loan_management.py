"""
NAME
    loan_management.py

DESCRIPTION
    This module provides functions to handle book borrowing and returning operations
    for customers in the library system.

    This script requires os, datetime, returnBookDecorator, and pandas modules to be installed within
    the Python environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    - borrow_books(customer_id, *args):
        Allows a customer to borrow books from the library.
            returns True if the customer was removed correctly / False if something went wrong.

    - return_book(customer_id, book):
        Allows a customer to return a borrowed book to the library.
            returns True if the customer was removed correctly / False if something went wrong.

EXAMPLES
- borrow_books(5488, "Quo Vadis", "Pan Tadeusz")
- return_book(5488, "Quo Vadis")
"""

import os
import datetime
from returnBookDecorator import decorator
import pandas as pd


def borrow_books(customer_id, *args):
    """
    Allows a customer to borrow books from the library.

    args:
        customer_id (int): The ID of the customer borrowing the books.
        *args (str): List of book titles to be borrowed.

    returns:
        bool: True if books are borrowed successfully, False otherwise.
    """

    time = datetime.date.today()
    next_month = time + datetime.timedelta(days=31)

    if os.path.exists("DATABASE"):
        df_book = pd.read_csv("Library/book.csv",
                              usecols=["ID", "AUTHOR", "TITLE", "PAGES", "CREATED", "UPDATED", "IS_BORROWED"],
                              index_col="ID")

        with open(f"DATABASE/{customer_id}.txt", "a") as file:
            for title in args:
                book = df_book[df_book["TITLE"] == title]
                author = book["AUTHOR"].values[0]
                pages = book["PAGES"].values[0]
                df_book.at[book.index[0], "IS_BORROWED"] = True
                df_book.to_csv("Library/book.csv")
                file.write(f"\nTITLE: {title}, AUTHOR: {author}, PAGES: {pages},"
                           f" BORROWED: {time}, DUE_DATE: {next_month}, RETURNED: False")
        return True

    else:
        print("Error - Database directory does not exist")
        return False


@decorator
def return_book(customer_id, title):
    """
    Allows a customer to return a borrowed book to the library.

    args:
        customer_id (int): The ID of the customer returning the book.
        book (str): Title of the book to be returned.

    returns:
        bool: True if the book is returned successfully, False otherwise.
    """

    time = datetime.date.today()
    if os.path.exists(f"DATABASE/{customer_id}.txt"):
        df_book = pd.read_csv("Library/book.csv", index_col="ID")

        with open(f"DATABASE/{customer_id}.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, 0):
            if f"TITLE: {title}" in line:
                lines[i] = lines[i].replace("False", f"{time}")

        with open(f"DATABASE/{customer_id}.txt", "w") as file:
            file.writelines(lines)

        book_index = df_book[df_book["TITLE"] == title].index[0]

        df_book.at[book_index, "IS_BORROWED"] = False
        df_book.to_csv("Library/book.csv")
        print("Books returned successfully!")
        return True

    else:
        print("Error - Customer's file does not exist")
        return False
