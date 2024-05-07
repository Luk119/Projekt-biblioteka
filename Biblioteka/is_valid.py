import pandas as pd


def phone_validation(number: str) -> bool:
    if len(number) != 9:
        return False
    else:
        return True


def is_updated(customer_id: int) -> bool:

    df_address = pd.read_csv("Library/address.csv", usecols=["ID"], index_col="ID")

    if customer_id in df_address.index.values:
        return True
    else:
        return False


def not_borrowed(*args):
    df_book = pd.read_csv("Library/book.csv", usecols=["TITLE", "IS_BORROWED"])
    list_not_borrowed = []

    for title in args:
        if title in df_book["TITLE"].values:
            if not df_book[df_book["TITLE"] == title]["IS_BORROWED"].values[0]:
                list_not_borrowed.append(title)
                print(f"{title} has been successfully borrowed")
            else:
                print(f"Book is not available, '{title}' is currently borrowed by other customer.")
        else:
            print(f"'{title}' does not exists in library database.")

    return list_not_borrowed


def is_valid_customer_id(customer_id):
    try:
        int(customer_id)

    except ValueError as e:
        print(e)
        return False
    except TypeError as e:
        print(e)
        return False

    return True
