"""
NAME
    book_management

DESCRIPTION
    This module allows the user to print the result of a simple equation,
    such as x+y, x-y, and others for various values of input parameters (x or x, y)

    This tool accepts file (.txt) that includes equation as text.

    This script requires ..... (name of package) be installed within the Python
    environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    * calculated_equation(f(x,y),x,y) - returns the value of f(x,y) for x,y where
    f(x) is equation eg. 2*x

    * calculated_fun(f(x,y),x,y) - returns the value of A*(x+y) for f(x,y) = addition
    or B*(x-y) for f(x,y) = subtraction; globals.py contains A,B.

    * calculated_equation_with_file(f(x),x) - returns the value of f(x) for x where
     f(x) is equation in equation.txt file

EXAMPLES
    calculated_fun(addition, x=2, y=3)
    calculated_equation(equation='2*x', x=5)
    calculated_equation_with_file(file='equation.txt', x=5)
"""


"""
This module contains functions to manage biblioteka books.
Module change their information in "Library/book.csv" filepath.
Module contains:
    -add_book()
    -delete_book()
    -print_books()
"""
import pandas as pd
import datetime
import os
def add_book(author, title, pages):
    """
    Function add_books takes 3 parameters: author, title, pages. Function will add a book to the "Library/books.csv" file
    contain information about ID, author, title, pages, created and updated.
    ID is generated automatically, have 4 numbers long. Created and Updated columns are current time dates.
    Args:
        author(str): The name and surname of the author
        title(str): The name of the book
        pages(str): The number of pages of the book

    Returns:
        True if book is added correctly
        False if is not added correctly
    """
    df = pd.read_csv("Library/book.csv", usecols=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'], index_col='ID')

    max_index = df.shape[0] + 1
    while max_index in df.index:
        max_index += 1

    time = datetime.date.today()
    df.loc[max_index] = [author, title, pages, time, time]
    df.to_csv("Library/book.csv")
def delete_book(id_or_title):
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
    df = pd.read_csv("Library/book.csv", usecols=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'], index_col='ID')
    print(df.head(1000))


