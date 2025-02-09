'''

Are you fully exploiting Python’s control structures?

Control structures are the backbone of any programming language, enabling you to dictate the flow of your code based on various
conditions and criteria. Python, with its simple and intuitive syntax, provides a range of control structures that make it easy
to write efficient, readable, and dynamic code. These structures allow you to perform tasks repeatedly, make decisions, and handle
exceptions seamlessly.

This comprehensive guide explores Python’s control structures through practical examples using climatic data, providing detailed
explanations and illustrative code samples.



If-else statements
Step 1: Basic if-else statement
The if-else statement allows you to execute code based on a condition. If the condition is true, the code block inside the if
statement is executed; otherwise, the code block inside the else statement is executed.

# Basic if-else example with climatic data
temperature = 30  # Temperature in Celsius

if temperature > 25:
    print("It's a hot day.")
else:
    print("It's a cool day.")

In this example, if the temperature is greater than 25°C, the program prints “It’s a hot day”; otherwise, it prints “It’s a cool day.”

Step 2: Elif statement
The elif (else if) statement allows you to check multiple conditions in sequence.

# Elif statement example with climatic data
temperature = 18  # Temperature in Celsius

if temperature > 30:
    print("It's very hot.")
elif temperature > 20:
    print("It's warm.")
elif temperature > 10:
    print("It's cool.")
else:
    print("It's cold.")

Here, the program evaluates the temperature and prints the corresponding message based on the range in which the temperature falls.

For loops
Step 1: Basic for loop
For loops in Python iterate over a sequence (like a list, tuple, string, or dictionary) and execute a block of code for each item in
the sequence.

# Basic for loop example with a list of temperatures
temperatures = [22.1, 23.5, 21.8, 24.0, 22.9]

for temp in temperatures:
    print(f"Temperature: {temp}°C")

In this example, the for loop iterates over each temperature in the list and prints it.

Step 2: Using range() in for loops
The range() function generates a sequence of numbers, which is particularly useful for looping a specific number of times.

# Using range() to iterate over a sequence of numbers

for i in range(5):
    print(f"Day {i+1}")

This loop prints “Day 1” to “Day 5”.

While loops
Step 1: Basic while loop
While loops execute a block of code repeatedly as long as a given condition is true.

# Basic while loop example with climatic data
temperature = 20  # Initial temperature in Celsius

while temperature < 25:
    print(f"Current temperature: {temperature}°C")
    temperature += 1

In this example, the loop prints the current temperature and increments it by 1 until it reaches 25°C.

Step 2: Avoiding infinite loops
Ensure you include a condition that eventually becomes false to avoid infinite loops.

# Infinite loop example
while True:
    print("This will print forever unless stopped.")
    break  # To stop the loop, use a break statement

Here, the loop runs forever but stops immediately due to the break statement.

Break, continue, and pass statements
Step 1: Using break
The break statement terminates the current loop prematurely.

# Using break to exit a loop when a specific temperature is reached
temperatures = [22.1, 23.5, 21.8, 24.0, 25.6, 26.7]

for temp in temperatures:
    if temp > 25:
        print(f"Temperature {temp}°C is too high! Stopping the loop.")
        break
    print(f"Temperature: {temp}°C")
In this example, the loop stops as soon as a temperature above 25°C is encountered.

Step 2: Using continue
The continue statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

# Using continue to skip certain temperatures
temperatures = [22.1, 23.5, 21.8, 24.0, 25.6, 26.7]

for temp in temperatures:
    if temp < 23:
        continue  # Skip temperatures less than 23°C
    print(f"Temperature: {temp}°C")
This loop skips temperatures less than 23°C and continues with the next iteration.

Step 3: Using pass
The pass statement is a null operation; it does nothing and is used as a placeholder for future code.

# Using pass as a placeholder in a loop
temperatures = [22.1, 23.5, 21.8, 24.0, 25.6, 26.7]

for temp in temperatures:
    if temp < 23:
        pass  # Placeholder for future code
    print(f"Temperature: {temp}°C")
In this example, the pass statement does nothing but indicates that some action might be added later for temperatures less than 23°C.

Exception handling
Step 1: Basic try-except block
Exception handling allows you to manage errors gracefully using try-except blocks.

# Handling errors in a loop
temperatures = [22.1, "23.5", 24.8, 25.6, 26.7]

for temp in temperatures:
    try:
        if temp > 25:
            print(f"High temperature {temp}°C detected! Stopping the loop.")
            break
        print(f"Temperature: {temp}°C")
    except TypeError:
        print(f"Invalid temperature data: {temp}")
        break
This loop handles any TypeErrors that occur during temperature monitoring.

Step 2: Using finally
The finally block executes code regardless of whether an exception is raised or not.

# Using finally to clean up resources
temperatures = [22.1, "23.5", 24.8, 25.6, 26.7]

for temp in temperatures:
    try:
        if temp > 25:
            print(f"High temperature {temp}°C detected! Stopping the loop.")
            break
        print(f"Temperature: {temp}°C")
    except TypeError:
        print(f"Invalid temperature data: {temp}")
    finally:
        print("Attempted to process temperature data.")

This loop ensures that the message “Attempted to process temperature data.” is printed after each iteration, regardless of whether
an exception occurred.

Practical applications with climatic data
Step 1: Monitoring temperature changes
Use a while loop to monitor and respond to temperature changes.

# Monitoring temperature changes
current_temperature = 20  # Initial temperature in Celsius

while current_temperature < 30:
    print(f"Current temperature: {current_temperature}°C")
    current_temperature += 0.5  # Simulate temperature increase

print("Temperature monitoring complete.")

In this example, the loop simulates temperature monitoring by incrementing the temperature and printing it.

Step 2: Collecting temperature data
Simulate collecting temperature data until a certain threshold is reached.

# Collecting temperature data
collected_data = []
current_temperature = 18

while current_temperature < 25:
    collected_data.append(current_temperature)
    print(f"Collected temperature: {current_temperature}°C")
    current_temperature += 1

print(f"Collected data: {collected_data}")
This loop collects temperature data until the temperature reaches 25°C and stores it in a list.

Step 3: Filtering data
Use a for loop with continue to filter temperatures above a certain threshold.

# Filtering temperatures above 23°C
high_temperatures = []

for temp in temperatures:
    if temp > 23:
        high_temperatures.append(temp)

print(f"High temperatures: {high_temperatures}")
This loop adds temperatures above 23°C to a new list.

Advanced techniques with control structures
Step 1: Combining loops and conditions
Combine loops and if-else statements for complex data processing.

# Combining loops and if-else for complex data processing
temperatures = [22.1, 23.5, 24.8, 25.6, 26.7]
humidity_levels = [60, 65, 70, 75, 80]

for temp, humidity in zip(temperatures, humidity_levels):
    if temp > 25:
        print(f"High temperature: {temp}°C, Humidity: {humidity}%")
    elif temp < 23:
        print(f"Low temperature: {temp}°C, Humidity: {humidity}%")
    else:
        print(f"Moderate temperature: {temp}°C, Humidity: {humidity}%")
This loop processes temperature and humidity data together, providing detailed information based on the values.

Step 2: Using else with loops
The else clause can be used with loops to execute a block of code once the loop condition is no longer true.

# Using else with while loop
temperature = 20

while temperature < 25:
    print(f"Temperature: {temperature}°C")
    temperature += 1
else:
    print("Temperature has reached 25°C or higher.")
In this example, the else block runs when the temperature reaches 25°C.

Real-world applications of control structures
Step 1: Simulating real-time data collection
Simulate real-time data collection using while loops and time delays.

# Simulating real-time temperature data collection
import random
import time

collected_temperatures = []

while len(collected_temperatures) < 10:
    current_temperature = random.uniform(18, 25)
    collected_temperatures.append(current_temperature)
    print(f"Collected temperature: {current_temperature:.2f}°C")
    time.sleep(1)  # Simulate delay

print(f"Collected temperatures: {collected_temperatures}")
This loop collects ten random temperature readings, simulating real-time data collection with a delay.

Step 2: Monitoring and alerting system
Create a simple monitoring and alerting system using control structures.

# Simple monitoring and alerting system
temperature = 20

while temperature < 30:
    if temperature > 25:
        print(f"Alert! High temperature: {temperature}°C")
        break
    print(f"Current temperature: {temperature}°C")
    temperature += 1
else:
    print("Temperature is within the safe range.")

In this example, the loop monitors the temperature and triggers an alert if it exceeds 25°C.

How to use control structures
Keep it simple: Avoid overly complex logic within control structures to enhance readability.
Use meaningful variable names: Ensure variable names clearly indicate their purpose.
Comment your code: Use comments to explain the purpose of complex control structures, making the code easier to understand.
Optimize performance: Be mindful of performance, especially when processing large datasets or running time-based loops.
Handle errors gracefully: Use try-except blocks to handle potential errors and ensure robust code execution.
Understanding and effectively using control structures in Python is crucial for managing the flow of your programs and writing dynamic,
efficient, and readable code. By exploring these concepts through real-world climatic data examples, you can better grasp how to apply
Python’s control structures to practical problems. This article has covered a wide range of topics, from basic if-else statements and
loops to advanced techniques and real-world applications.

In conclusion, mastering control structures in Python enables you to develop robust and maintainable code. By continuously practicing
and exploring Python’s capabilities, you can enhance your programming skills and solve real-world challenges more effectively. So,
dive into Python programming with these climatic data examples and discover how you can leverage the power of control structures to
improve your projects and data analysis workflows.
'''