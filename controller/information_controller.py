from service import information_service


# decorator
def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner

class InformationController:
    def __init__(self):
        self.service = information_service
