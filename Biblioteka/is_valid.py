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
