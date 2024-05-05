import os
def borrow_books(customer_id, *args):
    if os.path.exists("DATABASE"):
        with open(f"DATABASE/{customer_id}.txt", "a")as file:
            pass
    else:
        print("Error - Database directory does not exist")

    for book in args:
        pass

def return_book(customer_id, book):
    pass
