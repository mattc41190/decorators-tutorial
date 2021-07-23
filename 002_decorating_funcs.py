# What if instead of passing a value to the outer function, we passed ANOTHER function?
def decorator(fn_to_wrap):
    # Get the "message" from the function we passed to the the decorator function
    msg = fn_to_wrap()

    def wrapper_function():
        print(
            f"I am in the wrapper function and I have access to the decorator function message:\n{msg}"
        )
    # Like before we RETURN another function which can then be invoked and is aware of the context
    # in which it was made
    return wrapper_function

def get_hello():
    return "hello"

def get_bye():
    return "bye"

hello_func = decorator(get_hello)
bye_func = decorator(get_bye)

hello_func()
bye_func()