def length_logging_decorator(fn):
    print("I get called upon the wrapped function being decalred now!")
    print(f"The address in memory for the PASSED function: {fn}")
    def wrapper_function(*args, **kwargs):
        msg = fn(*args, **kwargs)
        print(f"Message Length: {len(msg)} \nMessage: {msg} \n")
    return wrapper_function


@length_logging_decorator
def hello(name):
    return f"hello {name}"

print(f"The address in memory for the DECORATED function: {hello}\n")

@length_logging_decorator
def bye(name):
    return f"bye {name}"

print(f"The address in memory for the DECORATED function: {bye}\n")

hello("matthew r cale")
bye("lindy")