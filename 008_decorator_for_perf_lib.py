def timed(fn):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"{fn.__name__} ran in {end_time - start_time} seconds\n")
        return result

    return wrapper


@timed
def cheap():
    max = 10000
    n = 0
    while n < max:
        n += 1
    print(f"I counted to {n}!")
    return n

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

print(f"small result: {small}")
print(f"big result: {big}")