from cProfile import Profile
from pstats import SortKey, Stats
import random

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

def nested_loop():
    total = 0
    for x in range(10_000):
        for y in range(10_000):
            x_squared = x ** 2
            y_squared = y ** 2
            total += x_squared + y_squared
    return total

def selection_sort():
    arr = [random.randint(1, 100) for _ in range(10_000)]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def basic_search():
    arr = [random.randint(1, 100) for _ in range(100_000)]
    arr.sort()

    for x in arr:
        if x == random.randint(1, 100):
            return True
    return False

def array_sum():
    total = 0
    squares = [x * x for x in range(1000000)]
    for x in squares:
        total += x

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def has_even_number():
    has_even = False
    arr = [i for i in range(1_000_000)]
    for x in arr:
        if x % 2 == 0:
            has_even = True
    return has_even

def read_file():
    with open('optims.py') as f:
        for line in f:
            print(line)

with Profile() as profile:
    print(f"{fib(35) = }")
    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CUMULATIVE)
        .print_stats()
    )
