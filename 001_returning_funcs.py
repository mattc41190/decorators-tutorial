# An example of a function return a function that has access to the context in which is was declared
def outer_function(msg):

    def inner_function():
        print(
            f"I am in the inner function and I have access to the outer function message:\n{msg}"
        )

    # The items that inner function has access to will be available 
    return inner_function

hello = "hello"
bye = "bye"

hello_func = outer_function(hello)
bye_func = outer_function(bye)

hello_func()
bye_func()

