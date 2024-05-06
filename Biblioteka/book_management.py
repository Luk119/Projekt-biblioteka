import pandas as pd
import datetime
import os
def add_book(author, title, pages):
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
            print("Brak książki w systemie o tych danych.")
            return 1

    df.to_csv("Library/book.csv", index=False)
    print("Książka została usunięta")

    return 0

def print_books():
    df = pd.read_csv("Library/book.csv", usecols=['ID', 'AUTHOR', 'TITLE', 'PAGES', 'CREATED', 'UPDATED'], index_col='ID')
    print(df.head(1000))


