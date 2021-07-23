class length_logging_with_call_stats_decorator(object):

    # We can keep state for all users of the decorator!
    total_uses = 0

    def __init__(self, fn):
        print(f"Creating new \"function\", or more correctly, new callable, based on {fn.__name__}")
        self.fn = fn
    
    # The __call__ method in this case can be invoked with the @ symbol
    # just as if it were a function decorator. The thing here is this
    def __call__(self, *args, **kwargs):
        length_logging_with_call_stats_decorator.total_uses += 1 
        print(f"The call method of {self} was invoked")
        msg = self.fn(*args, **kwargs)
        print(f"Message Length: {len(msg)} \nMessage: {msg} \n")


@length_logging_with_call_stats_decorator
def hello(name):
    return f"hello {name}"

@length_logging_with_call_stats_decorator
def bye(name):
    return f"bye {name}"

hello("matthew r cale")
bye("lindy")
hello("johnny be good")
bye("regina spektor")
hello("abe lincoln")



total = length_logging_with_call_stats_decorator.total_uses
print(f"METRICS: Total uses of length_logging_with_call_stats_decorator: {total}")