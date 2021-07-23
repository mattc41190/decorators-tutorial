# Here is the simplest example of using a decoarator to do something simple, but therhetically useful
def length_logging_decorator(fn_to_wrap):
    def wrapper_function():
        # Notice we do not HAVE to execute the function in the outer context
        # we CAN call the passed function on every call to the new wrapped function
        # think about how this might help if we wanted to pass args in the future?
        msg = fn_to_wrap()
        print(f"Message Length: {len(msg)} \nMessage: {msg} \n")
    return wrapper_function

def get_hello():
    return "hello"

def get_bye():
    return "bye"

hello_func = length_logging_decorator(get_hello)
bye_func = length_logging_decorator(get_bye)

hello_func()
bye_func()