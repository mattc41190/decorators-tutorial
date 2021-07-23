def pretty_info(fn):
    def wrapper(*args, **kwargs):
        # This will always show wrapper not cheap / expensive, but it does "WORK"
        # In next lesson we will fix this
        print(f"********** running: {fn.__name__} **********\n")
        result = fn(*args, **kwargs)
        print(f"********** done running: {fn.__name__} **********\n")
        return result 
    return wrapper

def timed(fn):
    import time

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