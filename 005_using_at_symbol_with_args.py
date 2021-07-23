# Switching from fn_to_wrap to simple fn
def length_logging_decorator(fn):
    def wrapper_function(*args, **kwargs):
        msg = fn(*args, **kwargs)
        print(f"Message Length: {len(msg)} \nMessage: {msg} \n")
    return wrapper_function

# Explanation of the @ Symbol: 
# Imagine the next few lines look like this:
# def hidden_hello(name):
#     return f"hello {name}"
# hello = length_logging_decorator(hidden_hello)
# you NEVER see hidden_hello and in truth the function "hello"
# in the remained of the seen context refers the wrapper_function 
# within: length_logging_decorator 

@length_logging_decorator
def hello(name):
    return f"hello {name}"

@length_logging_decorator
def bye(name):
    return f"bye {name}"

hello("matthew r kale")
bye("lindy")