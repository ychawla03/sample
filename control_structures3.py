'''

In Python, loops are control flow structures that allow you to repeatedly execute a block of
code. They are used to iterate over sequences, such as lists, strings, and other iterable
objects, to perform a set of operations multiple times. Python supports two main types of
loops: for loops and while loops.


1. For Loop with Range:
# This loop iterates over a range of numbers from 0 to 4.
for i in range(5):
    print(i)

2. For Loop with List:
# This loop iterates over each element in the list fruits.
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

3. While Loop:
# This while loop continues executing as long as the condition count < 5 is true.
count = 0
while count < 5:
    print(count)
    count += 1
4. Nested For Loops:
# This example shows nested loops,
# with the outer loop iterating 3 times and the inner loop iterating 2 times for each outer iteration.
for i in range(3):
    for j in range(2):
        print(i, j)
5. Looping Through Dictionary:
# This loop iterates over the key-value pairs of a dictionary.
student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
for name, grade in student_grades.items():
    print(name, grade)
6. Looping Through String:
# This loop iterates over each character in the string "Python".
for char in "Python":
    print(char)
7. Breaking Out of a Loop:
# This loop prints numbers from 0 to 9 but breaks out when i reaches 5.
for i in range(10):
    if i == 5:
        break
    print(i)
8. Continue Statement:
# This loop prints only odd numbers by skipping even numbers using the continue statement.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
9. Looping with Else Block:
# The else block is executed when the loop completes without encountering a break.
for i in range(5):
    print(i)
else:
    print("Loop finished without a break.")
10. Looping Through a File:
# This loop iterates through lines in a file.
with open('example.txt', 'r') as file:
    for line in file:
        print(line)
11. Looping with Enumerate:
# The enumerate function is used to iterate over both the index and value of the list.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
12. Looping with Zip:
# The zip function combines two lists element-wise for iteration.
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(name, age)
13. Looping with Range and Step:
# The range function with step 2 generates numbers from 0 to 8 (exclusive) with a step of 2.
for i in range(0, 10, 2):
    print(i)
14. Looping in Reverse:
# The reversed function reverses the order of the elements in the specified iterable.
for i in reversed(range(5)):
    print(i)
15. Looping with Sorted List:
# The sorted function returns a sorted version of the specified iterable.
numbers = [3, 1, 4, 1, 5, 9, 2]
for num in sorted(numbers):
    print(num)
16. Looping Until a Condition is Met:
# This while loop continues indefinitely until the break statement is triggered.
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break
17. Looping with List Comprehension:
# This uses list comprehension to create a list of squares of numbers from 0 to 4.
squares = [x**2 for x in range(5)]
print(squares)
18. Looping with Set Comprehension:
# Set comprehension is used to create a set of unique characters from the given string.
unique_chars = {char for char in 'abracadabra'}
print(unique_chars)
19. Looping with Dictionary Comprehension:
# This creates a dictionary using dictionary comprehension with keys as numbers and values as their squares.
square_dict = {x: x**2 for x in range(5)}
print(square_dict)
20. Looping with If-Else Inside:
# An if-else statement is used inside the for loop to print whether each number is even or odd.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Even" if num % 2 == 0 else "Odd")
21. Looping Over a String with Index:
# This loop iterates over each character in a string using the index.
word = "Python"
for i in range(len(word)):
    print(word[i])
22. Looping with a Step and Range:
# The range function is used with a step of 3 to generate numbers from 0 to 9.
for i in range(0, 10, 3):
    print(i)
23. Looping through a Tuple:
# This loop iterates over each element in a tuple.
colors = ('red', 'green', 'blue')
for color in colors:
    print(color)
24. Looping with Break and Else:
# The else block is executed only if the loop completes without encountering a break.
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop completed without break.")
25. Looping through a 2D List:
# This nested loop iterates through elements of a 2D list (matrix).
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)
26. Looping with Pass:
# The pass statement is a no-op, used as a placeholder.
for i in range(5):
    pass  # Placeholder for future code
27. Looping with numpy for Mathematical Operations:
# numpy is used for numerical operations, and here it's used to create and loop through a matrix.
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for row in matrix:
    print(row)
28. Looping with datetime for Date Range:
# datetime is used for working with dates, and here it's used to iterate over a date range.
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 5)

current_date = start_date
while current_date <= end_date:
    print(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)
29. Looping with sorted and reverse:
# This loop sorts the numbers list in descending order using the sorted() function with the reverse=True argument
# and then iterates over the sorted numbers, printing each one.
numbers = [4, 2, 7, 1, 9]
for num in sorted(numbers, reverse=True):
    print(num)
30. Looping with set for Unique Elements:
# This loop creates a set (unique_colors) from the colors list, which removes duplicate elements,
# and then iterates over the unique colors in the set, printing each unique color.
colors = ['red', 'green', 'blue', 'red', 'yellow']
unique_colors = set(colors)
for color in unique_colors:
    print(color)
31. Looping with Dictionary Items:
# This loop iterates over the items (key-value pairs) in the person dictionary and prints each key-value pair.
person = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
for key, value in person.items():
    print(f"{key}: {value}")
32. Looping with the iter() Function:
# The iter() function is used to create an iterator from a list.
numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)
for num in iter_numbers:
    print(num)
33. Looping with enumerate and Starting Index:
# The enumerate function is used with a starting index of 1.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
34. Looping with try and except for Error Handling:
# The try and except blocks handle potential errors during iteration.
numbers = [1, 2, 'three', 4, 'five']
for item in numbers:
    try:
        result = int(item)
        print(result)
    except ValueError:
        print(f"Cannot convert {item} to int.")
35. Looping with try and except for File Reading:
# try and except are used to handle file reading and potential file-not-found errors.
try:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
36. Looping with filter() and a Lambda Function:
# This loop uses the filter() function with a lambda function to create an iterable (even_numbers) containing only the even numbers from the numbers list.
# The for loop then iterates over this filtered iterable and prints each even number.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
for num in even_numbers:
    print(num)
37. Looping with map() and a Function:
# This loop uses the map() function to apply a lambda function that squares each number in the numbers list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
for num in squared_numbers:
    print(num)
38. Looping with reduce() and a Function:
# This loop calculates the product of all numbers in the numbers list using the functools.reduce function and a lambda function.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
39. Looping through a String in Reverse:
# This loop iterates over the characters of the string "Python" in reverse order and prints each character on a new line.
# The reversed() function is used to reverse the order of the characters in the string.
word = "Python"
for char in reversed(word):
    print(char)
40. Looping with any() and all() functions:
# any() returns True if at least one element is true;
# all() returns True if all elements are true.
bool_values = [True, False, True, True]
print(any(bool_values))  # True if at least one True
print(all(bool_values))  # True if all are True
41. Looping with all for Check All True:
# checks whether all conditions in the conditions list are True.
conditions = [True, True, True, False]
if all(conditions):
    print("All conditions are true")
42. Looping with break and else in a While Loop:
# else block in a while loop is executed if the loop completes without encountering a break.
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("While loop completed without break.")
43. Looping through a Dictionary’s Keys:
# Looping through the keys of a dictionary using the keys() method.
student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
for name in student_grades.keys():
    print(name)
44. Looping through a Dictionary’s Values:
# Looping through the values of a dictionary using the values() method.
student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
for grade in student_grades.values():
    print(grade)
45. Looping with itertools.cycle:
# itertools.cycle is used to create an infinite loop cycling through elements.
from itertools import cycle

colors = ['red', 'green', 'blue']
infinite_colors = cycle(colors)
for _ in range(10):
    print(next(infinite_colors))
46. Looping with itertools.cycle and zip for Circular Iteration:
# itertools.cycle is used for circular iteration along with zip.
colors = ['red', 'green', 'blue']

for color, index in zip(cycle(colors), range(8)):
    print(f"Step {index + 1}: {color}")
47. Looping with itertools.count:
# itertools.count generates an infinite sequence of numbers starting from a specified value.
from itertools import count

for i in count(start=1, step=2):
    if i > 10:
        break
    print(i)
48. Looping with itertools.accumulate:
# itertools.accumulate is used to compute the cumulative sum of the elements.
from itertools import accumulate

numbers = [1, 2, 3, 4, 5]
cumulative_sum = accumulate(numbers)
for total in cumulative_sum:
    print(total)
49. Looping with itertools.permutations:
# itertools.permutations generates all possible permutations of a sequence.
from itertools import permutations

letters = ['A', 'B', 'C']
perms = permutations(letters)
for perm in perms:
    print(perm)
50. Looping with itertools.combinations:
# itertools.combinations generates all combinations of a specified length.
from itertools import combinations

letters = ['A', 'B', 'C']
combs = combinations(letters, 2)
for comb in combs:
    print(comb)
51. Looping with itertools.product:
# itertools.product is used to create Cartesian product of the lists.
from itertools import product

dice = [1, 2, 3, 4, 5, 6]
outcomes = product(dice, repeat=2)
for outcome in outcomes:
    print(outcome)
52. Looping with enumerate and Unpacking:
# enumerate is combined with unpacking to iterate over both index and values in tuples.
matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for row, (a, b, c) in enumerate(matrix):
    print(row, a, b, c)
53. Looping with try and finally:
# The finally block is executed regardless of whether an exception is caught.
for i in range(5):
    try:
        result = 10 / (i - 3)
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        print("This will always execute.")
54. Looping with collections.Counter:
# collections.Counter is used to count occurrences of elements in a list.
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
for word, count in word_counts.items():
    print(word, count)
55. Looping with collections.Counter for Finding Most Common Elements:
# collections.Counter is used to count occurrences of elements,
# and most_common is used to find the most common elements.
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)

most_common = word_counts.most_common(2)

for word, count in most_common:
    print(word, count)
56. Looping with collections.defaultdict:
#collections.defaultdict is used to count occurrences with a default value of 0.
from collections import defaultdict

fruit_counts = defaultdict(int)
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
for fruit in fruits:
    fruit_counts[fruit] += 1
print(fruit_counts)
57. Looping with break and continue in Nested Loops:
# break and continue are used in nested loops.
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
        if i == 1:
            break
58. Looping with asyncio for Asynchronous Programming:
# Demonstrates the use of asyncio for asynchronous programming.
import asyncio

async def example_coroutine():
    print("Start Coroutine")
    await asyncio.sleep(1)
    print("End Coroutine")

loop = asyncio.get_event_loop()
loop.run_until_complete(example_coroutine())
59. Looping with async for in Asynchronous Programming:
#Uses async for to iterate asynchronously within an asynchronous coroutine.
import asyncio

async def example_coroutine():
    for i in range(3):
        print(f"Step {i}")
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(example_coroutine())
60. Looping with time.sleep for Time Delays:
# time.sleep is used to introduce a delay between iterations.
import time

for i in range(5):
    print(i)
    time.sleep(1)
61. Looping through a List Backwards:
# reversed is used to iterate through the list in reverse order.
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)
62. Looping with functools.lru_cache for Memoization:
# functools.lru_cache is used for memoization in a recursive Fibonacci function.
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i))
63. Looping with os.listdir to Iterate Over Files in a Directory:
# os.listdir is used to iterate over files in a directory.
import os

directory_path = '/path/to/directory'

for file_name in os.listdir(directory_path):
    print(file_name)
64. Looping with sorted and Custom Key Function:
# sorted is used with a custom key function to sort by the length of strings.
words = ['apple', 'banana', 'orange', 'grape']
for word in sorted(words, key=len):
    print(word)
65. Looping with itertools.islice for Slicing Iterables:
# itertools.islice is used to slice an iterable.
from itertools import islice

numbers = range(10)
for num in islice(numbers, 3, None, 2):
    print(num)
66. Looping with functools.partial to Create Partial Functions:
# The loop uses the functools.partial function to create specialized functions for squaring and cubing
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

for i in range(5):
    print(square(i), cube(i))
67. Looping with functools.partial and map:
# functools.partial is used to create a partially-applied function, and map applies it to a list.
from functools import partial

cube = partial(pow, exponent=3)
numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)
for result in cubed_numbers:
    print(result)
68. Looping with bytearray for Manipulating Bytes:
# The for loop is used to iterate over each element (byte) in the bytearray named data.
# In each iteration, the variable byte takes on the value of the current byte in the bytearray.
data = bytearray(b'hello')
for byte in data:
    print(byte)
69. Looping with enumerate and Tuple Unpacking:
# enumerate and tuple unpacking are used to loop over multiple lists.
countries = ['USA', 'Canada', 'UK']
capitals = ['Washington', 'Ottawa', 'London']
for index, (country, capital) in enumerate(zip(countries, capitals)):
    print(f"{index + 1}. {country} - {capital}")
70. Looping with zip and Unpacking in a List Comprehension:
# zip and list comprehension are used to create a list of formatted strings.
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
formatted_data = [f"{name} is {age} years old" for name, age in zip(names, ages)]
for info in formatted_data:
    print(info)
71. Looping with enumerate and zip in a Dictionary Comprehension:
# enumerate and zip are used in a dictionary comprehension to create a dictionary.
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
data_dict = {name: age for name, age in zip(names, ages)}
for name, age in data_dict.items():
    print(f"{name} is {age} years old")
72. Looping with shutil to Iterate Over Files in a Directory:
# The for loop iterates over each item in the list, and in each iteration, the variable file takes the value of the current item.
import shutil

for file in shutil.listdir('/path/to/directory'):
    print(file)
73. Looping with os.walk to Traverse Directory Tree:
# os.walk is used to traverse a directory tree, iterating over folders, subfolders, and files.
import os

for folder, subfolders, files in os.walk('/path/to/directory'):
    for file in files:
        print(os.path.join(folder, file))
74. Looping with functools.reduce for Cumulative Operations:
# functools.reduce is used to perform a cumulative operation on the elements of an iterable.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
75. Looping with itertools.chain to Flatten Lists:
# itertools.chain is used to flatten a list of lists.
from itertools import chain

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = list(chain(*nested_lists))
print(flattened_list)
76. Looping with contextlib.suppress for Suppressing Exceptions:
# contextlib.suppress is used to suppress specific exceptions.
from contextlib import suppress

numbers = [1, 2, 'three', 4, 'five']
for item in numbers:
    with suppress(ValueError):
        result = int(item)
        print(result)
77. Looping with collections.namedtuple:
# collections.namedtuple is used to create a simple class with named fields.
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
points = [Point(1, 2), Point(3, 4), Point(5, 6)]

for point in points:
    print(f"X: {point.x}, Y: {point.y}")
78. Looping with functools.partialmethod:
# functools.partialmethod is used to create a partially-applied method.
from functools import partialmethod

class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, x):
        return x * self.multiplier

double = partialmethod(Multiplier, 2)

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double().multiply, numbers)

for result in doubled_numbers:
    print(result)
79. Looping with itertools.dropwhile:
# itertools.dropwhile skips elements until a certain condition becomes false.
from itertools import dropwhile

numbers = [1, 3, 5, 2, 4, 6]
for num in dropwhile(lambda x: x % 2 == 1, numbers):
    print(num)
80. Looping with functools.wraps for Decorator:
# functools.wraps is used to preserve the original function's information in a decorator.
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
81. Looping with subprocess for Running External Commands:
# subprocess is used to run external commands and capture their output.
import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
for line in result.stdout.split('\n'):
    print(line)
82. Looping with threading for Parallel Execution:
# threading is used for parallel execution of a function.
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
83. Looping with multiprocessing for Parallel Processing:
# multiprocessing is used for parallel processing of a function.
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()
84. Looping with requests for HTTP Requests:
# requests is used to make HTTP requests.
import requests

response = requests.get('https://www.example.com')
for line in response.text.split('\n')[:5]:
    print(line)
85. Looping with re for Regular Expression Matching:
# re is used for regular expression matching.
import re

pattern = re.compile(r'\b\w{3,}\b')
text = "This is an example text with some words."

for word in re.findall(pattern, text):
    print(word)
86. Looping with itertools.groupby:
# itertools.groupby is used to group consecutive elements based on a key function.
from itertools import groupby

animals = [('cat', 1), ('dog', 2), ('cat', 3), ('dog', 4), ('cat', 5)]

for animal, group in groupby(animals, key=lambda x: x[0]):
    print(animal, list(group))
87. Looping with asyncio.gather for Concurrent Asynchronous Tasks:
# asyncio.gather is used to run multiple asynchronous tasks concurrently.
import asyncio

async def task_one():
    await asyncio.sleep(1)
    print("Task One")

async def task_two():
    await asyncio.sleep(2)
    print("Task Two")

asyncio.run(asyncio.gather(task_one(), task_two()))
88. Looping with collections.deque for Efficient Queue Operations:
# collections.deque is used for efficient queue operations.
from collections import deque

queue = deque([1, 2, 3, 4, 5])

while queue:
    print(queue.popleft())
89. Looping with traceback for Exception Information:
# traceback is used to print detailed information about an exception.
import traceback

def example_function():
    raise ValueError("An example error.")

try:
    example_function()
except ValueError as e:
    traceback.print_exc()
90. Looping with contextlib.ExitStack for Dynamic Context Management:
# contextlib.ExitStack is used for dynamic context management.
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ['file1.txt', 'file2.txt']]
    for file in files:
        print(file.readline().strip())
91. Looping with heapq for Heap Operations:
# heapq is used for heap operations, and here it's used to create and pop elements from a min-heap.
import heapq

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
heapq.heapify(numbers)

while numbers:
    print(heapq.heappop(numbers))
92. Looping with functools.cmp_to_key for Custom Sorting:
# functools.cmp_to_key is used for custom sorting using a comparison function.
from functools import cmp_to_key

def custom_sort(x, y):
    return len(x) - len(y)

words = ['apple', 'banana', 'orange', 'grape']
sorted_words = sorted(words, key=cmp_to_key(custom_sort))

for word in sorted_words:
    print(word)
93. Looping with collections.ChainMap for Combining Dictionaries:
# collections.ChainMap is used to combine dictionaries.
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = dict(ChainMap(dict1, dict2))

for key, value in combined_dict.items():
    print(key, value)
94. Looping with itertools.takewhile for Taking Elements:
# itertools.takewhile is used to take elements while a certain condition is true.
from itertools import takewhile

numbers = [1, 3, 5, 2, 4, 6]
taken_numbers = list(takewhile(lambda x: x % 2 == 1, numbers))

for num in taken_numbers:
    print(num)
95. Looping with itertools.zip_longest for Zipping Uneven Iterables:
# itertools.zip_longest is used to zip uneven iterables with a fill value for missing elements.
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]

for name, age in zip_longest(names, ages, fillvalue='N/A'):
    print(f"{name} is {age} years old")
96. Looping with warnings.simplefilter for Controlling Warnings:
# warnings.simplefilter is used to control the display of warnings.
import warnings

warnings.simplefilter('ignore', category=DeprecationWarning)

def deprecated_function():
    print("This is a deprecated function.")

deprecated_function()
97. Looping with queue.Queue for Thread-Safe Queue:
# queue.Queue is used for a thread-safe queue.
import threading
import queue

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processed: {item}")
        q.task_done()

q = queue.Queue()

for i in range(3):
    threading.Thread(target=worker, args=(q,), daemon=True).start()

for item in range(5):
    q.put(item)

q.join()

for _ in range(3):
    q.put(None)

q.join()
98. Looping with concurrent.futures.ThreadPoolExecutor for Concurrent Thread Execution:
# concurrent.futures.ThreadPoolExecutor is used for concurrent execution using threads.
from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x ** 2

with ThreadPoolExecutor() as executor:
    numbers = [1, 2, 3, 4, 5]
    results = list(executor.map(square, numbers))

for result in results:
    print(result)
99. Looping with contextlib.nullcontext for Null Context Management:
# contextlib.nullcontext is used for creating a null context manager.
from contextlib import nullcontext

with nullcontext():
    print("This code is executed with a null context.")
100. Looping with while and User Input:
# This example demonstrates a while loop that continues until the user inputs "quit" (case-insensitive).
user_input = ''
while user_input.lower() != 'quit':
    user_input = input("Enter something (type 'quit' to exit): ")
    print(f"You entered: {user_input}")
101. Looping with while and Random Numbers:
# This example uses a while loop to generate random guesses until the guess matches a target number.
import random

target_number = 7
guess = 0
while guess != target_number:
    guess = random.randint(1, 10)
    print(f"Guessed: {guess}")
102. Looping with random.choice for Random Selection:
# random.choice is used to randomly select an element from a sequence.
import random

colors = ['red', 'green', 'blue']

for _ in range(3):
    print(random.choice(colors))
103. Looping with datetime.timedelta for Date Range:
# datetime.timedelta is used to represent differences between dates.
from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 5)

current_date = start_date
while current_date <= end_date:
    print(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)
104. Looping with while and File Reading:
# This while loop reads lines from a file until there are no more lines.
with open('sample.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
105. Looping with while and Timeout:
# The while loop runs until a timeout of 5 seconds is reached, simulating a task with a time limit.
import time

timeout = time.time() + 5  # 5 seconds from now
while time.time() < timeout:
    print("Performing a task...")
    time.sleep(1)
106. Looping with while and Password Input:
# This example uses a while loop for password validation, repeatedly asking the user for input until the correct password is entered.
password = 'secret'
user_input = ''
while user_input != password:
    user_input = input("Enter the password: ")
    if user_input != password:
        print("Incorrect password. Try again.")
print("Login successful!")
107. Looping with while and User Confirmation:
# The while loop prompts the user for confirmation, and it continues until the user inputs "yes" (case-insensitive).
user_confirmation = 'no'
while user_confirmation.lower() != 'yes':
    user_confirmation = input("Are you sure? (yes/no): ")
    if user_confirmation.lower() != 'yes':
        print("Please confirm with 'yes'.")
print("Confirmed!")
108. Looping with while and Input Validation:
# This example demonstrates a while loop for input validation, ensuring the user enters a numeric value.
valid_input = False
while not valid_input:
    user_age = input("Enter your age: ")
    if user_age.isdigit():
        valid_input = True
    else:
        print("Invalid input. Please enter a number.")
print(f"Your age is: {user_age}")
109. Looping with while and Fibonacci Sequence:
# The while loop generates Fibonacci numbers until reaching a value greater than or equal to 100.
a, b = 0, 1
while a < 100:
    print(a, end=', ')
    a, b = b, a + b
110. Looping with while and Progress Bar:
# This example uses a while loop to simulate a progress bar updating until the total iterations are reached.
import time

total_iterations = 10
current_iteration = 0
while current_iteration < total_iterations:
    print(f"Progress: {current_iteration}/{total_iterations}", end='\r')
    time.sleep(0.5)
    current_iteration += 1
111. Looping with while and Graceful Shutdown:
# Looping with while and Graceful Shutdown:
import signal
import sys

def signal_handler(sig, frame):
    print("\nGraceful shutdown initiated.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    print("Performing a task...")


'''