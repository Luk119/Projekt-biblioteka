import pandas as pd
import datetime
import os
def add_customer(name, email, password):
    df = pd.read_csv("Library/customer.csv", usecols=['ID', 'NAME', 'E-MAIL', 'PHONE', 'CREATED', 'UPDATED'])

    max_index = df.shape[0] + 1
    while max_index in df.index:
        max_index += 1

    time = datetime.date.today()
    df.loc[max_index] = [author, title, pages, time, time]
    print(df.head(5))
    df.to_csv("Library/book.csv")