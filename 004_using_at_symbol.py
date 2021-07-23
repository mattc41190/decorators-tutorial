def length_logging_decorator(fn_to_wrap):
    def wrapper_function():
        msg = fn_to_wrap()
        print(f"Message Length: {len(msg)} \nMessage: {msg} \n")
    return wrapper_function


@length_logging_decorator
def get_hello():
    return "hello"

@length_logging_decorator
def get_bye():
    return "bye"

get_hello()
get_bye()