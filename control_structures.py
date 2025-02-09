'''
Control Structures in Python: Condition statements, loops and exception handling

python control structures:
Control structures are an essential part of programming that allow you to specify the flow of execution in your code.
In Python, there are several types of control structures including:


Conditional statements: These statements allow you to execute certain code blocks only if a certain condition is met. For example,
you might want to check if a number is even or odd before performing some operation on it. In Python, the conditional statements
are if, elif, and else.

Loops: Loops allow you to execute a block of code multiple times. Python has two types of loops: for loops and while loops. For loops
are used to iterate over a sequence of elements (such as a list), while while loops are used to repeat a block of code as long as a
certain condition is true.

Exception handling: Exception handling allows you to handle errors that may occur in your code gracefully, without causing the
program to crash. In Python, you can use the try and except statements to handle exceptions.

Control structures are an important concept in programming, as they allow you to write code that can adapt to different input,
make decisions based on conditions, and repeat actions. By using control structures effectively, you can write more powerful and
flexible programs.

Conditional statements (if-else)
In Python, the if statement is used to execute a block of code if a certain condition is true. Here is the general syntax for
an if statement:

if condition:
    # code to be executed if condition is true

Here is an example of an if statement in Python:

x = 10
if x > 5:
    print("x is greater than 5")

In this example, the condition x > 5 is true, so the code block print(“x is greater than 5”) will be executed.

The elif (short for “else if”) statement is used to specify additional conditions that should be checked if the condition
in the previous if statement is false. Here is the general syntax for an elif statement:

elif condition:
    # code to be executed if condition is true
Here is an example of using elif statements in Python:

x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")

In this example, the condition x > 5 is false, so the code block print(“x is greater than 5”) will not be executed. The condition
x > 5 is false, so the condition x == 5 would be checked, and the code block print(“x is equal to 5”) is executed because x = 5.

The else statement is used to specify a block of code that should be executed if none of the previous conditions are true. Here is
the general syntax for an else statement:

else:
    # code to be executed if all previous conditions are false

Here is an example of using else statements in Python:

x = 4
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

In this example, the condition x > 5 is false, so the code block print(“x is greater than 5”) will not be executed. The condition
x > 5 is false, so the condition x == 5 is checked, but the code block print(“x is equal to 5”) is not executed because is false.
Since both of these conditions were false, the code block print(“x is less than 5”) is executed.

You can use if, elif, and else statements together to create complex control structures that can make decisions based on multiple
conditions.

Loops (for, while)
Loops in Python allow you to execute a block of code repeatedly, either a specified number of times or until a certain condition is
met. There are two types of loops in Python: for loops and while loops.

for loops
A for loop in Python iterates over a sequence of elements, such as a list or a string. Here is the general syntax for a for loop:

for element in sequence:
    # code to be executed

Here is an example of a for loop that iterates over a list of numbers and prints out each number:

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

Output:
1
2
3
4
5
You can also use the range() function to specify the number of iterations in the loop. The range() function returns a sequence of
numbers, starting from 0 by default, and increments by 1 (also by default), and ends at a specified number.Here is an example of
using range() in a for loop:

for i in range(5):
    print(i)

Output:
0
1
2
3
4

You can also specify a start and end value for the range() function, like this:

for i in range(2, 5):
    print(i)
Output:
2
3
4

You can even specify a step value, which determines how much the loop variable is incremented each iteration. For example, the
following for loop will count by twos:

for i in range(0, 10, 2):
    print(i)
Output:
0
2
4
6
8

while loops
A while loop in Python executes a block of code repeatedly until a certain condition is met. The syntax for a while loop is as follows:

while condition:
    # code to be executed

Here is an example of a while loop that counts from 1 to 5:

i = 1
while i <= 5:
    print(i) i += 1

Output:
1
2
3
4
5

It’s important to include a way to change the value of the loop condition, or else the loop will run forever (called an “infinite loop”).
In the example above, we increase the value of i by 1 each iteration using the += operator.

Break and continue
In Python, the break statement is used to exit a loop prematurely. When the break statement is encountered in the code, the program
control immediately exits the current loop, and continues with the next statement after the loop. This allows you to exit a loop
early, when a certain condition is met, rather than continuing to iterate until the end of the loop.

Here is an example of using the breakstatement in a for loop:

for i in range(10):
    if i == 5:
        break
    print(i)

Output:
0
1
2
3
4

In this example, the loop iterates over the range from 0 to 9, but the breakstatement exits the loop when i is equal to 5, so only
the numbers from 0 to 4 are printed.

It’s also possible to use breakin while loop, such as:

i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print(i)

Output:
1
2
3
4

As you can see here the while loop only runs 4 times and breaks out of the loop when i becomes equal to 5.

It’s important to be careful when using break statement as if it's not used properly it might lead to an infinite loop or miss
certain conditions, making the code to stop running even when it should not. Also, note that it only breaks out of the nearest
enclosing loop and the control goes to the next statement after the loop.

In Python, the continue statement is used to skip the current iteration of a loop, and continue with the next iteration. When the
continue statement is encountered in the code, the current iteration of the loop is immediately terminated, and the program control
proceeds to the next iteration of the loop. This allows you to selectively skip certain iterations of the loop, rather than
completely ending the loop altogether.

Here is an example of using the continue statement in a for loop:

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

Output:
1
3
5
7
9

In this example, the loop iterates over the range from 0 to 9, but the continue statement skips all the even numbers (i.e., those
for which i % 2 == 0 is true), and only odd numbers are printed.

It’s also possible to use continue in while loop.

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

Output:
1
3
5
7
9

As you can see the continue statement here skips the even number which makes the loop only print the odd numbers starting from 1

It’s important to be careful when using continue statement as if it's not used properly it might lead to an infinite loop and
unexpected results.

Exceptions
Exceptions in Python are a mechanism to handle errors and exceptional conditions in the program execution. An exception is
raised (or thrown) when a certain condition or error occurs in the code. When an exception is raised, the program execution
stops and the program control jumps to the nearest exception handler. If an exception is not handled, it will cause the
program to terminate.

To handle exceptions in Python, you use a try-except block. The code that may raise an exception is placed in the try block,
and the code to handle the exception is placed in the except block. Here's an example:

try:
    x = 1 / 0
except ZeroDivisionError:
    print("division by zero")

In this example, a ZeroDivisionError exception is raised when trying to divide 1 by 0, which is caught by the except block and a
message is printed.

You can also have multiple except block to handle multiple exception.

try:
    x = 1 / 0
except ZeroDivisionError:
    print("division by zero")
except Exception as e:
    print("an exception occurred: ", e)

It’s important to note that the order of the except block matter, Python will execute the first except block that it finds that
matches the type of exception that was raised.

You can also use the else block to specify code that should be executed when no exception is raised in the try block. This code will
only be executed if all the statements in the try block are executed without raising any exception.

try:
    x = 1 / 1
except ZeroDivisionError:
    print("division by zero")
else:
    print("operation successfull")

The finally block is used to specify code that should be executed regardless of whether an exception is raised or not.
Code in the finally block will always be executed, whether an exception is raised or not.

try:
    x = 1 / 0
except ZeroDivisionError:
    print("division by zero")
finally:
    print("this will always be printed")

Another way to raise an exception is using the raise statement which can be used to raise a user-defined exception.

if x < 0:
    raise ValueError("x should be non-negative")

It’s important to handle exceptions properly to make sure your code runs smoothly and prevent unexpected termination. And also
note that one can also create custom exception by deriving from the base exception class Exception or any other exception class.

It’s also a best practice to raise exceptions as early as possible to make the debugging process easier.
'''