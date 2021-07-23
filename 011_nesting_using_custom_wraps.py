# Example of how I see imagine functools @wraps works:
def wraps(original_fn):

    def wrapped_wrapper_fn(wrapper_fn):
        def inner_wrapper(*args, **kwargs):
            return wrapper_fn(*args, **kwargs)
        inner_wrapper.__name__ = original_fn.__name__
        inner_wrapper.__doc__ = """lets freaking party..."""
        return inner_wrapper

    return wrapped_wrapper_fn

def pretty_info(fn):

    # wraps is a decorator which accepts a function, AND it takes a wrapper for said function
    # So we can picture it like this: wraps(orig, wrapper) -> wrapper with modified insides
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"********** running: {fn.__name__} **********\n")
        result = fn(*args, **kwargs)
        print(f"********** done running: {fn.__name__} **********\n")
        return result 
    return wrapper

def timed(fn):
    import time

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"{fn.__name__} ran in {end_time - start_time} seconds\n")
        return result

    return wrapper

@pretty_info
@timed
def cheap():
    max = 10000
    n = 0
    while n < max:
        n += 1
    print(f"I counted to {n}!")
    return n

@pretty_info
@timed
def expensive():
    max = 10000000
    n = 0
    while n < max:
        n += 1
    print(f"I counted to {n}!")
    return n

small = cheap()
big = expensive()

# That's a wrap