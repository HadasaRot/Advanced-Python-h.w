import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"Time for {func.__name__}: {finish - start} seconds")
        return result
    return wrapper


def cache(func):
    all_last_result = {}
    def wrapper(n):
        if n in all_last_result:
            return all_last_result[n]
        all_last_result[n] = func(n)
        return all_last_result[n]

    return wrapper

@execution_time
def print_n(n):
    for i in range(n):
        j =1

@execution_time
def add(a, b):
    return a + b


@execution_time
def find_number_in_list(number, n=100000):
    _list = list(range(n))
    return number in _list

@execution_time
def sort_numbers(numbers):
    return sorted(numbers)

@cache
@execution_time
def fibonacci_with_cache(n):
    if n <= 1 :
        return n
    return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)


@execution_time
def fibonacci_without_cache(n):
    if n <= 1 :
        return n
    return fibonacci_without_cache(n-1) + fibonacci_without_cache(n-2)


print(fibonacci_with_cache(10))
print(fibonacci_without_cache(10))


arr = [5,4,8,34,1,12,34,1,9,99,7,6,5,67,5,44,3,7,6,4,3,23,24,25,65,3,2,6,7,7,8,2,1,0,9,7,56,43,3]
print_n(50000000)
add(1, 2)
find_number_in_list(50000)
sort_numbers(arr)
