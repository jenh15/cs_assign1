def decorator(func):
    def wrapper(*args):
        result = args[0] + args[1]
        print("The result is", result)
        return result
    return wrapper

@decorator
def add(x, y):
    return x + y

add(1, 2)