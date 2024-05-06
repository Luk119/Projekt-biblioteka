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

    Args:
        customer_id (int): The ID of the customer borrowing the books.
        *args (str): List of book titles to be borrowed.

    returns:
        bool: True if books are borrowed successfully, False otherwise.
    """

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
        print("Books borrowed successfully!")
        return True

    else:
        print("Error - Database directory does not exist")
        return False


@decorator
def return_book(customer_id, book):
    """
        Allows a customer to return a borrowed book to the library.

        Args:
            customer_id (int): The ID of the customer returning the book.
            book (str): Title of the book to be returned.

        returns:
            bool: True if the book is returned successfully, False otherwise.
    """

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
        return True

    else:
        print("Error - Customer's file does not exist")
        return False
