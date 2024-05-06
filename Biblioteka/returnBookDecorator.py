def decorator(func):
    def wrapper(customer_id, *args):
        for title in args:
            func(customer_id, title)
    return wrapper
