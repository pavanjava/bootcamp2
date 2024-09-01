import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"{func.__name__} executed in: {execution_time:.6f} seconds")
        return result

    return wrapper
