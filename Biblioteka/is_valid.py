import pandas as pd


def phone_validation(number: str) -> bool:
    """
    Checks if the phone number is 9-digit long.

    args:
        number (str): The phone number to be validated.

    returns:
        bool: True if the phone number is valid, False otherwise.
    """
    if len(number) != 9:
        return False
    else:
        return True


def is_updated(customer_id: int) -> bool:
    """
    Checks if the customer's address is updated.

    args:
        customer_id (int): The ID of the customer.

    returns:
        bool: True if the address is updated, False otherwise.
    """

    df_address = pd.read_csv("Library/address.csv", usecols=["ID"], index_col="ID")

    if customer_id in df_address.index.values:
        return True
    else:
        return False


def not_borrowed(*args: str) -> list:
    """
    Checks if the given books are available for borrowing.

    args:
        *args (str): Variable number of book titles to be checked.

    returns:
        list: List of book titles that are available for borrowing.
    """
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
            print(f"Error '{title}' does not exists in library database.")

    return list_not_borrowed


def is_valid_customer_id(customer_id: int) -> bool:
    """
    Checks if the given customer ID is valid.

    args:
        customer_id: The ID of the customer.

    returns:
        bool: True if the customer ID is valid, False otherwise.
    """
    try:
        int(customer_id)

    except ValueError as e:
        print("Error", e)
        return False
    except TypeError as e:
        print("Error", e)
        return False

    return True
