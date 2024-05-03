import pandas as pd
import datetime
import random
def add_customer(action, name, email, phone):

    if len(phone) != 9:
        print("Phone number is invalid")
        print("User was not registered")
        return 1

    if action == 1:

        #
        df = pd.read_csv("Library/customer.csv", usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'],index_col='ID')

        time = datetime.date.today()
        id = random.randint(1000, 9999)
        while True:
            if id in df.index:
                id = random.randint(1000, 9999)
                continue
            else:
                break

        df.loc[id] = [name, email, int(phone), time, time]
        df.to_csv("Library/customer.csv")
        #
        print("Klient dodany pomyślnie")
    elif action == 2:
        pass

def remove_customer(id):
    pass