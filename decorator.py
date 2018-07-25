# decorator
# a callable, input is callable, output is callable

# Case 1
def null_decorator(func):
    return func

def greet():
    return "Case1"

greet = null_decorator(greet)
print(greet())


# Case 1 of another representation
@null_decorator
def greet():
    return 'Case another'
print(greet())



# Case 2
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello! uppercase!'

print(greet())
