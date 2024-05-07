"""
NAME
    customer_management.py

DESCRIPTION
    This module allows the user to manage customers in the library system.
    It provides functionality to add, update, and remove customer records.

    This script requires pandas, datetime, random, os, and is_valid module to be installed within
    the Python environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    - add_customer(name, email, phone):
        Adds a new customer to the library system.
            returns True if the customer was added correctly / False if something went wrong.

    - update_customer_address(customer_id, street, city, country):
        Updates the address of a customer in the library system.
            returns True if the customer address was added correctly / false if something went wrong.

    - remove_customer(customer_id=None, name=""):
        Removes a customer from the library system.
        It can be done by providing either customer ID or name.
            returns True if the customer was removed correctly / False if something went wrong.

    - print_customers():
        Prints the information about all customers from the library system.
            returns nothing

EXAMPLES
- add_customer("Tomasz Nowak", "tomasz.nowak123@gamil.com", "503931449")
- update_customer_address(5488, "Pogodna 22", "Nowe miasto", "Polska")
- remove_customer(customer_id=5488)
- remove_customer(name="Tomasz Nowak")
"""
import pandas as pd
import datetime
import random
import os
import is_valid as iv


def add_customer(name, email, phone):
    """
    Adds a new customer to the library system.

        Args:
            name (str): The name of the customer.
            email (str): The email address of the customer.
            phone (str): The phone number of the customer.

        returns:
            bool: True if the customer is added correctly, False otherwise.
    """

    if not iv.phone_validation(phone):
        print("Phone number is invalid")
        print("User was not registered")
        return False

    try:
        df = pd.read_csv("Library/customer.csv",
                         usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],
                         index_col='ID')

    except FileNotFoundError as e:
        print(e)
        return False

    time = datetime.date.today()
    customer_id = random.randint(1000, 9999)

    while customer_id in df.index:
        customer_id = random.randint(1000, 9999)

    df.loc[customer_id] = [name, email, int(phone), time, "False"]
    df.to_csv("Library/customer.csv")

    if os.path.exists("DATABASE"):
        with open(f"DATABASE/{customer_id}.txt", "w") as file:
            file.write(f"Books lend by {name} user: ")

    else:
        print("Error - Database directory does not exist")

    print("Customer created correctly, client file was successfully added")
    return True


def update_customer_address(customer_id, street, city, country):
    """
    Updates the address of a customer in the library system.

    Args:
        customer_id (int): The ID of the customer whose address is to be updated.
        street (str): The street of the customer's address.
        city (str): The city of the customer's address.
        country (str): The country of the customer's address.

    returns:
        None
    """
    df_customer = pd.read_csv("Library/customer.csv")

    if customer_id in df_customer["ID"].values:
        df_address = pd.read_csv("Library/address.csv", index_col='ID')
        df_address.loc[customer_id] = [street, city, country]
        df_address.to_csv("Library/address.csv")

        time = datetime.date.today()

        df_customer = pd.read_csv("Library/customer.csv",
                                  usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],
                                  index_col="ID")

        df_customer['UPDATED'] = df_customer['UPDATED'].astype(str)
        df_customer.loc[customer_id, "UPDATED"] = str(time)
        df_customer.to_csv("Library/customer.csv")

        print(f"The Customer {customer_id} has been successfully updated.")
    else:
        print("The customer does not exist")


def remove_customer(customer_id=None, name=""):
    """
        Removes a customer from the library system.

        Args:
            customer_id (int, optional): The ID of the customer to be removed.
            name (str, optional): The name of the customer to be removed.

        returns:
            bool: True if the customer is removed correctly, False otherwise.
    """

    df_customer = pd.read_csv("Library/customer.csv",
                              usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],
                              index_col='ID')

    df_address = pd.read_csv("Library/address.csv",
                             usecols=['ID', "STREET", "CITY", "COUNTRY"],
                             index_col="ID")

    if customer_id is not None:
        if customer_id not in df_customer.index.values:
            print("Error - A customer with given id has not been created.")
            return False
        else:
            df_customer = df_customer.drop(customer_id)
            df_customer.to_csv("Library/customer.csv")
            print(f"Customer {customer_id} removed from 'customer.csv' file")

        if customer_id not in df_address.index.values:
            print(f"Error - Customer {customer_id} has no data in 'address.csv' file")
        else:
            df_address = df_address.drop(customer_id)
            df_address.to_csv("Library/address.csv")
            print(f"Customer {customer_id} removed from 'address.csv' file")

        if os.path.exists(f"DATABASE/{customer_id}.txt"):
            os.remove(f"DATABASE/{customer_id}.txt")
            print(f"Customer {customer_id} removed from 'DATABASE/{customer_id}.txt' file")
        else:
            print(f"Error - Customer {customer_id} has no data in 'DATABASE/{customer_id}.txt' file")

        return True

    else:
        if name not in df_customer["NAME"].values:
            print("Error - A customer with the given name and surname has not been created.")
            return False

        try:
            id_from_name = df_customer[df_customer['NAME'] == name].index.values[0]

        except IndexError as e:
            print(e)
            return False

        if id_from_name in df_customer:
            df_customer = df_customer.drop(id_from_name)
            df_customer.to_csv("Library/customer.csv")
            print(f"Customer {id_from_name} removed from 'customer.csv' file")
        else:
            print(f"Error - Customer {id_from_name} has no data in 'customer.csv' file")

        if id_from_name not in df_address.index.values:
            print(f"Error - Customer {id_from_name} has no data in 'address.csv' file")

        else:
            df_address = df_address.drop(id_from_name)
            df_address.to_csv("Library/address.csv")
            print(f"Customer {id_from_name} removed from 'address.csv' file")

        if not os.path.exists(f"DATABASE/{id_from_name}.txt"):
            print(f"Error - Customer {id_from_name} has no data in '{id_from_name}.txt' file")

        else:
            os.remove(f"DATABASE/{id_from_name}.txt")
            print(f"Customer {id_from_name} removed from 'DATABASE/{id_from_name}.txt' file")

        return True
def print_customers():
    """
    Prints information about all customers stored in the "Library/books.csv" file.

    returns:
        nothing
    """
    df_customer = pd.read_csv("Library/customer.csv",
                              usecols=['ID', 'NAME', 'E-MAIL', 'PHONE'],
                              index_col='ID')

    print(df_customer.head(1000))
