import pandas as pd
import datetime
import random
import os
def add_customer(name, email, phone):

    if len(phone) != 9:
        print("Phone number is invalid")
        print("User was not registered")
        return 1

    df = pd.read_csv("Library/customer.csv", usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],index_col='ID')

    time = datetime.date.today()
    id = random.randint(1000, 9999)

    while id in df.index:
        id = random.randint(1000, 9999)

    df.loc[id] = [name, email, int(phone), time, time]
    df.to_csv("Library/customer.csv")

    if os.path.exists("DATABASE"):
        with open (f"DATABASE/{id}.txt", "w")as file:
            pass

    else:
        print("Error - Database directory does not exist")

    print("Klient dodany pomyślnie, plik klienta utworzony")

def update_customer_address(customer_id, street, city, country):
    df_address = pd.read_csv("Library/address.csv", index_col='ID')
    df_address.loc[customer_id] = [street, city, country]
    df_address.to_csv("Library/address.csv")

def remove_customer(customer_id=None, name=""):
    df_customer = pd.read_csv("Library/customer.csv", usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],index_col='ID')
    df_address = pd.read_csv("Library/address.csv", usecols=['ID', "STREET", "CITY", "COUNTRY"], index_col="ID")

    if customer_id is not None:
        if customer_id not in df_customer.index.values:

            return 1

        df_customer = df_customer.drop(customer_id)
        df_customer.to_csv("Library/customer.csv")
        print(f"Customer {customer_id} removed from 'customer.csv'")

        if customer_id not in df_address.index.values:
            print(f"Brak danych klienta {customer_id} w pliku 'address.csv'")
            return 0

        df_address = df_address.drop(customer_id)
        df_address.to_csv("Library/address.csv")
        print(f"Customer {customer_id} removed from 'address.csv'")
        return 0

    else:
        if name not in df_customer["NAME"].values:
            return 1

        try:
            id_from_name = df_customer[df_customer['NAME'] == name].index.values[0]

        except IndexError as e:
            print(e)
            return 1

        df_customer = df_customer.drop(id_from_name)
        df_customer.to_csv("Library/customer.csv")
        print(f"Customer {id_from_name} removed from 'customer.csv'")

        if id_from_name not in df_address.index.values:
            print(f"Brak danych klienta {id_from_name} w pliku 'address.csv'")
            return 0

        df_address = df_address.drop(id_from_name)
        df_address.to_csv("Library/address.csv")
        print(f"Customer {id_from_name} removed from 'address.csv'")

        return 0




