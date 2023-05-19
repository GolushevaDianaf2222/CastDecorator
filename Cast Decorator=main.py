
def cast(to_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return to_type(result)
            except (ValueError, TypeError):
                print(f"Unable to cast result to type {to_type}")
                return result
        return wrapper
    return decorator
 

