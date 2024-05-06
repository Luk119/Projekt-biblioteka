"""
NAME
    book_management.py

DESCRIPTION
    This module allows the user to manage books in
    'Library/book.csv' file and print all book information.

    This script requires pandas, datatime, os be installed within
    the Python environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    - add_book(author, title, pages):
        Adds a book to the library
            returns True if the book was added correctly / False if something went wrong
    
    - delete_book(id_or_title):
        Deletes a book from the library
            returns True if the book was deleted correctly / False if something went wrong
    
    - print_books():
        Prints all the books and their information in the library
            returns: nothing

EXAMPLES
- add_book("Henryk Sienkiewicz", "Quo Vadis", 297)
- delete_book(23) or delete_book("Quo Vadis")
- print_books()
        
"""

import pandas as pd
import datetime
import os


def add_book(author: str, title: str, pages: str) -> bool:
    """
     Adds a book to the "Library/books.csv" file containing information about ID, author, title, pages, created, and updated.

    Args:
        author (str): The name and surname of the author.
        title (str): The name of the book.
        pages (str): The number of pages of the book.

    Returns:
        bool: True if the book is added correctly, False if it is not added correctly.
    """
    df = pd.read_csv("Library/book.csv", usecols=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'], index_col='ID')

    max_index = df.shape[0] + 1
    while max_index in df.index:
        max_index += 1

    time = datetime.date.today()
    df.loc[max_index] = [author, title, pages, time, time]
    df.to_csv("Library/book.csv")


def delete_book(id_or_title):
    """
    Deletes a book from the "Library/books.csv" file based on the provided ID or title.

    Args:
        id_or_title (str): ID or title of the book to be deleted.

    Returns:
        bool: True if the book is deleted correctly, False otherwise.
    """
    df = pd.read_csv("Library/book.csv")

    if id_or_title.isdigit():
        if int(id_or_title) in df["ID"].values:
            df = df.drop(df[df["ID"] == int(id_or_title)].index)

    else:
        if id_or_title in df["TITLE"].values:
            df = df.drop(df[df["TITLE"] == id_or_title].index)

        else:
            print("The data does not match any book")
            return False

    df.to_csv("Library/book.csv", index=False)
    print("Book was successfully deleted")

    return True


def print_books():
    """
    Prints information about all books stored in the "Library/books.csv" file.

    Returns:
        None
    """
    df = pd.read_csv("Library/book.csv", usecols=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'], index_col='ID')
    print(df.head(1000))


