def decorator(func):
    """
    Decorator function to handle book returning operations.

    Args:
        func (function): Function to be decorated.

    returns:
        function: Wrapper function.
    """
    def wrapper(customer_id, *args):
        for title in args:
            func(customer_id, title)
    return wrapper
