import pandas as pd
import datetime
import random
import os
import is_valid as iv
def add_customer(name, email, phone):

    if not iv.phone_validation(phone):
        print("Phone number is invalid")
        print("User was not registered")
        return False

    df = pd.read_csv("Library/customer.csv", usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],index_col='ID')

    time = datetime.date.today()
    customer_id = random.randint(1000, 9999)

    while customer_id in df.index:
        customer_id = random.randint(1000, 9999)

    df.loc[customer_id] = [name, email, int(phone), time, time]
    df.to_csv("Library/customer.csv")

    if os.path.exists("DATABASE"):
        with open(f"DATABASE/{customer_id}.txt", "w")as file:
            file.write(f"Books lend by {name} user: ")

    else:
        print("Error - Database directory does not exist")

    print("Customer created correctly, client file was successfully added")

def update_customer_address(customer_id, street, city, country):
    df_address = pd.read_csv("Library/address.csv", index_col='ID')
    df_address.loc[customer_id] = [street, city, country]
    df_address.to_csv("Library/address.csv")

def remove_customer(customer_id=None, name=""):
    df_customer = pd.read_csv("Library/customer.csv", usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'], index_col='ID')
    df_address = pd.read_csv("Library/address.csv", usecols=['ID', "STREET", "CITY", "COUNTRY"], index_col="ID")


    if customer_id is not None:
        if customer_id not in df_customer.index.values:
            print("Error - A customer with given id has not been created.")
            return False
        else:
            df_customer = df_customer.drop(customer_id)
            df_customer.to_csv("Library/customer.csv")
            print(f"Customer {customer_id} removed from 'customer.csv' file")

        if customer_id not in df_address.index.values:
            print(f"Customer {customer_id} has no data in 'address.csv' file")
        else:
            df_address = df_address.drop(customer_id)
            df_address.to_csv("Library/address.csv")
            print(f"Customer {customer_id} removed from 'address.csv' file")

        if os.path.exists(f"DATABASE/{customer_id}.txt"):
            os.remove(f"DATABASE/{customer_id}.txt")
            print(f"Customer {customer_id} removed from 'DATABASE/{customer_id}.txt' file")
        else:
            print(f"Customer {customer_id} has no data in 'DATABASE/{customer_id}.txt' file")

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
            print(f"Customer {id_from_name} has no data in 'customer.csv' file")


        if id_from_name not in df_address.index.values:
            print(f"Customer {id_from_name} has no data in 'address.csv' file")

        else:
            df_address = df_address.drop(id_from_name)
            df_address.to_csv("Library/address.csv")
            print(f"Customer {id_from_name} removed from 'address.csv' file")


        if not os.path.exists(f"DATABASE/{id_from_name}.txt"):
            print(f"Customer {id_from_name} has no data in '{id_from_name}.txt' file")

        else:
            os.remove(f"DATABASE/{id_from_name}.txt")
            print(f"Customer {id_from_name} removed from 'DATABASE/{id_from_name}.txt' file")

        return True




