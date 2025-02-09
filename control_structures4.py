'''

Lists : An Ordered Mutable Collection of Objects in Python

Let’s dig deeper into lists with some build-in methods in python , list Comprehension , 
Indexing, Slicing, Control Structures and Functions


Python comes with four build-in data structures that we can use to hold any collection of objects,
one among them is List. Whenever we have a bunch of related objects and we need to put them
somewhere in code , List are the perfect choice. Python’s list is less restrictive. We can have
a list of objects and each object can be of a different type. We can also change a list at any
time by adding, removing or changing objects .Besides being heterogeneous and mutable , lists
are dynamic i.e they can grow and shrink on demand.Lists are enclosed in square brackets and
objects within it are separated by comma. In this article, we shall learn about some of the more
frequently used methods , functions and various operations which makes list different form other
data structures.

1. Python’s Build-in Methods
1.1 append( )
The append() method adds a new object to the end of a list. The length of the list increases by one.

Syntax : list.append(object), where :

object is a number, a string or another list[Required]
Example:

fruit_list = ['apple', 'mango']
fruit_list.append('banana')
print (fruit_list)
#Output
['apple', 'mango', 'banana']
1.2 extend( )
The extend() method appends all elements of a list to the another list. Iterates over the argument of a list and adding each
element to the other list ,thus, extending the list. The length of the list increases by number of elements in it’s argument.
append() and extend() methods can only add elements at the end.

Syntax : list.extend(iterable), where :

iterable is another list that gets appended to the list [Required]
Example:

fruit_list = ['apple', 'mango', 'banana']
num_list = [6, 0, 4, 1]
fruit_list.extend(num_list)
print (fruit_list)

#Output
['apple', 'mango', 'banana', 6, 0, 4, 1]

1.3 insert( )
The insert() method insert an item at the specific position in the list. Unlike append() which takes only one argument, insert()
method requires two arguments, position and value to be added at respective position.

Syntax : list.insert(position,value), where :

position is the index of the element before which the value is inserted[Required]
value or element which is to be inserted in the list[Required]
Example:

fruit_list = ['apple', 'mango', 'banana', 6, 0, 4, 1]
fruit_list.insert(2,'apricot')
print (fruit_list)
#Output
['apple', 'mango', 'apricot', 'banana', 6, 0, 4, 1]

1.4 remove( )
The remove() method delete the first occurrence of specified element from the list. It only removes one element at a time, to
remove range of elements, iterator can be used. It raises a ValueError if there is no such element.

Syntax : list.remove(value), where :

value or element which is to be removed from the list[Required]
Example:

fruit_list = ['apple', 'mango', 'apricot', 'banana', 6, 0, 4, 1]
fruit_list.remove('mango')
print (fruit_list)
#Output
['apple', 'apricot', 'banana', 6, 0, 4, 1]

1.5 pop( )
The pop() method removes and returns an element at the given position in the list.list.pop()removes and returns the last item in 
a list if position is not specified.This helps us implement lists as stacks (first in, last out data structure).

Syntax : list.pop(position) , where :

position is the index of the element which is to be removed from the list[Optional]
Example:

#position is not specified
fruit_list = ['apple', 'apricot', 'banana', 6, 0, 4, 1]
fruit_list.pop()
print (fruit_list)
#position is specified
fruit_list.pop(4)
print (fruit_list)
#Output
['apple', 'apricot', 'banana', 6, 0, 4]
['apple', 'apricot', 'banana', 6, 4]

1.6 del statement
The del method deletes all the elements in range mentioned in arguments.This differs from the pop()and remove()method and which 
removes single element . The del statement can also be used to remove slices from a list or clear the entire list .

Syntax : del list[start : end], where :

start is the index of the element from where the removal starts[Optional]
end is the index of the element before which the element is removed[Optional]
Example:

#start and end index to delete a range
fruit_list = ['apple', 'apricot', 'banana', 6, 4]
del fruit_list[2:4]
print (fruit_list)
#Delete the entire list
del fruit_list
#print (fruit_list)
#output
['apple', 'apricot', 4]
The above print statement will display an error “NameError: name ‘fruit_list’ is not defined” as the complete list is deleted.

1.7 clear( )
The clear() method erase all the elements from the list. After this operation, list becomes empty.

Syntax : list.clear()

Example:

animal_list = ['elephant','bear','zebra','kangaroo']
animal_list.clear()
print (animal_list)
#output
[]

1.8 index( )
The index() method returns the index ( zero-based index) of the first matched item in the list. If element searched is not present ,
then it returns a ValueError. The arguments start and end are optional and used to limit the search to a particular sub-sequence of
the list.

Syntax : list.index(element, start, end) , where :

element whose lowest index will be returned[Required]
start is the position from where the search begins[Optional]
end is the position where the search ends[Optional]
Example:

animal_list = ['elephant','bear','zebra','kangaroo']
animal_list.index('zebra')
#output
2
#index method will search the element within this range of start and end position
animal_list.index('kangaroo',1,4)
#output
3

1.9 count( )
The count() method returns the number of occurrence of element passed as an argument in the list. It can return count of single
element at a time.

Syntax : list.count(element) , where :

element whose count is to be returned[Required]
Example:

animal_list = ['elephant','bear','zebra','kangaroo','elephant']
animal_list.count('elephant')
#output
2

1.10 sort( )
The sort() method sort elements in a list in both ascending order and descending order. By default, sort() doesn’t require any
extra parameters. However, it has two optional parameters that can be used for sort customization .It returns a sorted list based
on the passed parameters.

Syntax :

list.sort()-- sorts in ascending order
list.sort(reverse=True)-- sorts in descending order
list.sort(key=<parameter>, reverse=<True/False>)-- customized sorting
reverse decides the sorting order [Optional]
key is the function or parameter which serves as a key for the sort comparison(customized sorting) [Optional]
Example:

#default sorting # ascending order
animal_list = ['elephant','bear','zebra','kangaroo']
animal_list.sort()
print (animal_list)
#descending order sorting
animal_list.sort(reverse=True)
print (animal_list)
#default sorting # ascending order for numbers
num_list = [6, 0, 4, 1]
num_list.sort()
print (num_list)
#descending order sorting
num_list.sort(reverse=True)
print (num_list)
#output
['bear', 'elephant', 'kangaroo', 'zebra']
['zebra', 'kangaroo', 'elephant', 'bear']
[0, 1, 4, 6]
[6, 4, 1, 0]
1.11 reverse( )
The reverse() method reverses the order of elements of the list in-place.

Syntax : list.reverse()

Example:

animal_list = ['elephant','bear','zebra','kangaroo']
animal_list.reverse()
print (animal_list)
num_list = [6, 0, 4, 1]
num_list.reverse()
print (num_list)
#output
['kangaroo', 'zebra', 'bear', 'elephant']
[1, 4, 0, 6]

1.12 copy( )
The copy() methods are always of a great utility whenever there is a need to reuse the object .It returns a shallow copy
(any modification done in copied list won’t be reflected to original list) of the list.

Syntax : list.copy()

Example:

#shallow copy
animal_list = ['elephant','bear','zebra','kangaroo']
copy_list = animal_list.copy()
print (copy_list)
#adding an element to the old list will not affect new list
animal_list.append('rabbit')
print (animal_list)
print (copy_list)
#output
['elephant', 'bear', 'zebra', 'kangaroo']
['elephant', 'bear', 'zebra', 'kangaroo', 'rabbit']
['elephant', 'bear', 'zebra', 'kangaroo']

2. Python’s Build-in Functions with List
Besides build-in methods, python consists of build-in functions. Below are some of the widely used built-in functions with List.
The Python documentation is an excellent source for more on build-in Functions.

2.1 sum( )
sum() — It Sums up the numbers in the list and returns the total.

Syntax : sum(<iterable>,start), where :

iterable is sequence(can be list , set , tuples or dictionaries) and it should contain numbers [Required]
start is added to the sum of numbers in the iterable [Optional]
Example:

num_list = [9, 12, 6, 0, 4, 1, 8]

# start parameter is not provided
Sum = sum(num_list)
print(Sum)

# start = 10, this will add 10 to the sum
Sum = sum(num_list, 10)
print(Sum)
#output
40
50

2.2 ord( )
ord() — Returns an integer representing the Unicode code point of the given Unicode character(a string of length one). If more than
one character is passed, a TypeError is raised.

Syntax : ord(<character>), where :

character is a Unicode character(a string of length one)[Required]
Example:

print(ord('a'))
print(ord('A'))
print(ord('$'))
print(ord('@'))
#output
97
65
36
64

2.3 max( )
max() — Returns largest element of the list or the largest of two or more arguments. If the list with elements as string, max( ) is
applicable. max( ) would return a string element whose ASCII value is the highest . Note that only the first index of each element
is considered each time and if the value is the same then second index is considered ,so on and so forth. If we want to find the
max( ) element based on the some specific criteria (e.g length of the element ) then another parameter ‘key’ is declared inside
the max( ) function.

Syntax : max(<iterable>,key=<parameter>), where :

iterable is sequence(can be list, set , tuples or dictionaries) [Required]
key is the function or parameter which serves as a key for comparison [Optional]
Example:

num_list = [9, 12, 6, 0, 4, 1, 8]
max(num_list)
#another parameter 'key=len' is declared to find the max string element based on the length of the string
animal_list = ['elephant','bear','zebra','kangaroo']
print(max(animal_list, key=len))
#output
12
elephant

2.4 min( )
min() —Return smallest element of the list or the smallest of two or more arguments. If the list with elements as string, min( ) is
applicable. min( ) would return a string element whose ASCII value is the lowest. Note that only the first index of each element is
considered each time and if the value is the same then second index is considered ,so on and so forth. If we want to find the min( )
element based on the some specific criteria (e.g length of the element ) then another parameter ‘key’ is declared inside the min( )
function.

Syntax : min(<iterable>,key=<parameter>), where :

iterable is sequence(can be list, set, tuples or dictionaries) [Required]
key is the function or parameter which serves as a key for comparison [Optional]
Example:

num_list = [9, 12, 6, 0, 4, 1, 8]
min(num_list)
#another parameter 'key=len' is declared to find the min string element based on the length of the string
animal_list = ['elephant','bear','zebra','kangaroo']
print(min(animal_list, key=len))
#output
0
bear

2.5 all( )
all() — Returns true if all element in the list are true or if list is empty. It can be It can be used for successive AND operations.
It short circuit the execution (stop the execution as soon as the result is known).

Syntax : all(<itreable>)

iterable is sequence(can be list, set, tuples or dictionaries) [Required]
Example:

# Since all are false, false is returned
print (any([False, False, False, False]))

# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False]))

# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False]))
#output
False
True
True

Table for ‘any’ and ‘all’ situations and their results

2.6 any( )
any() — Returns true if any element of the list is true. If list is empty or all are false, return false.It can be used for successive
Or operations . It short circuit the execution (stop the execution as soon as the result is known).

Syntax : any(<itreable>)

iterable is sequence(can be list, set, tuples or dictionaries) [Required]
Example:

# Here all the iterables are True so all
# will return True and the same will be printed
print (all([True, True, True, True]))

# Here the method will short-circuit at the
# first item (False) and will return False.
print (all([False, True, True, False]))

# This statement will return False, as no
# True is found in the iterables
print (all([False, False, False]))
#output
True
False
False

2.7 len( )
len() — Returns an integer which is the length or size of the argument. The argument can be a list, set, dictionary, string or any
other sequence or collection.

Syntax : len(<parameter>)

parameter is collection or sequence[Required]

Example:

num_list = [9, 12, 6, 0, 4, 1, 8]
len(num_list)
#output
7
animal_list = ['elephant','bear','zebra','kangaroo']
len(animal_list)
#output
4

2.8 enumerate( )
enumerate() — Adds a counter to an iterable. It returns enumerate object of a sequence which is a tuple containing a count and the
values obtained from iterable.

Syntax : enumerate(<iterable>,start=0)

iterable is sequence(can be list , set or dictionaries) [Required]
start is the index from which the counter is to be started, default value is 0 [Optional]
Example:

cities_list = ["New York","Farmington","Harrisburg","Washington","Baltimore"]
city = "Baltimore"

cities_enum = enumerate(cities_list)
print (list(cities_enum))
#changing start index to 2 from 0
city_enum = enumerate(city,2)
print (list(city_enum))
#output
[(0, 'New York'), (1, 'Farmington'), (2, 'Harrisburg'), (3, 'Washington'), (4, 'Baltimore')]
[(2, 'B'), (3, 'a'), (4, 'l'), (5, 't'), (6, 'i'), (7, 'm'), (8, 'o'), (9, 'r'), (10, 'e')]

3. List Indexing and Slicing
3.1 List Indexing
Lists can be indexed using square brackets to retrieve the element stored in a particular position. Index starts from 0.
Indexing is exactly similar to indexing in strings except that indexing in lists returns the entire item at that position whereas
in strings, the character at that position is returned.

Negative indexing
Negative sequence indexes represent positions from the end of the array. The index of -1 refers to the last item, -2 to the second
last item and so on.

Syntax: list[<index>]

index is the position of element in the list[Required]
Example:

#Indexing
vowel_list = ['a','e','i','o','u']
print(vowel_list[0])
print(vowel_list[4])
#Negative indexing
print(vowel_list[-5])
print(vowel_list[-1])
#output
a
u
a
u
3.2 List Slicing
Indexing was only limited to accessing a single element, Slicing on the other hand is accessing a sequence of data inside the list.
In other words “slicing” the list. The slicing operator used is :(colon) .

Slicing is done by defining the index values of the first element and the last element from the parent list that is required in the
sliced list. It is written as parent list[ a : b ] where a,b are the index values from the parent list. If a or b is not defined
then the index value is considered to be the first value for a if a is not defined and the last value for b when b is not defined.
It has 3 arguments with the last one being the optional index increment.

Syntax: list[start : stop : step]

So , [: stop] will slice list from starting till stop index and [start : ] will slice list from start index till end . Negative value
of steps shows right to left traversal instead of left to right traversal that is why [: : -1] prints list in reverse order.

start is the index from where the slicing of list begins[Optional]
stop is the index before which the slicing of list ends[Optional]
step is the gap taken between start and stop ,which means that slicing will start from index start will go up to stop in step.[Optional]
Example:

num_list = [9, 12, 6, 0, 4, 1, 8]
print(num_list[0:4])
print(num_list[4:])
#output
[9, 12, 6, 0]
[4, 1, 8]

4. List comprehensions : From loops to comprehensions
Python comprehensions are syntactic constructs that enable sequences to be built from other sequences in a clear and concise manner.
For Example , we want to create a list of first 10 multiple of 5 , So this can be done with a normal for loop or with list
comprehensions, Let’s see both of them and understand the difference.

4.1 Applying list comprehension
Syntax: [<expression> for <element> in <iterable>]

expression is operation need to be performed on the elements of iterable[Required]
iterable is sequence( list ) [Required]
element is the item from iterable[Required]
Example:

#Normal For loop
num_list = [1,2,3,4,5,6,7,8,9,10]
empty_list =[]
for n in num_list:
    empty_list.append(n*5)
print(empty_list)
#List comprehension
list_comp = [n*5 for n in num_list]
print(list_comp)
#Output:
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
We got the same output using list comprehensions just by writing a line of code.

4.2 Applying list comprehension with a condition
Syntax: [<expression> for <element> in <iterable> if <condition>]

expression is operation need to be performed on the elements of iterable[Required]
iterable is sequence( list ) [Required]
element is the item from iterable[Required]
condition- operation/expression is applied only for those elements whose condition is met[optional]
Example:

Now, Suppose we need to create a list of multiple of 5 for just even numbers.

# using a for loop and if condition
num_list = [1,2,3,4,5,6,7,8,9,10]
empty_list =[]
for n in num_list:
    if n%2==0:
        empty_list.append(n*5)
print(empty_list)
#Using list comprehensions
list_comp = [n*5 for n in num_list if n%2==0]
print(list_comp)
#Output:
[10, 20, 30, 40,  50]
[10, 20, 30, 40,  50]
4.3 Applying list comprehension with if-else condition
Syntax: [<expression> if <condition> else <other_expression> for <element> in <iterable>]

expression/other_expression is operation need to be performed on the elements of iterable[Required]
iterable is sequence( list ) [Required]
element is the item from iterable[Required]
condition- operation/expression is applied only for those elements whose condition is met[optional]
Example:

create a list of multiple of 6 for even numbers between 1 to 10 and multiple of 10 for rest of the numbers.

# using a for loop and with if-else condition
num_list = [1,2,3,4,5,6,7,8,9,10]
empty_list =[]
for n in num_list:
    if n%2==0:
        empty_list.append(n*6)
    else:
        empty_list.append(n*10)
print(empty_list)
#Using list comprehensions
list_comp = [n*6 if n%2==0 else n*10 for n in num_list]
print(list_comp)
#Output:
[10, 12, 30, 24, 50, 36, 70, 48, 90, 60]
[10, 12, 30, 24, 50, 36, 70, 48, 90, 60]

4.4 Applying list comprehension with Nested loops
Syntax: [<expression> for <element_a> in <iterable_a> (optional if <condition_a>)for <element_b> in <iterable_b> (optional if
<condition_b>) for <element_c> in <iterable_c> (optional if <condition_c>)...and so on]

expression is operation need to be performed on the elements of iterable[Required]
iterable is sequence( list ) [Required]
element is the item from iterable[Required]
condition- operation/expression is applied only for those elements whose condition is met[optional]
Example:

Now, we want to multiply numbers ranging from 1 to 10 with first 1 then 2 and then 3 and then 4.

#using Nested loops
num_list1 = [1,2,3,4]
num_list2 = [1,2,3,4,5,6,7,8,9,10]
empty_list =[]
for i in num_list1:
    for j in num_list2:
        empty_list.append(i*j)
print(empty_list)
#Using list comprehensions
list_comp = [i*j for i in num_list1 for j in num_list2 ]
print(list_comp)
#Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
5. Lambda expression : The anonymous function
Lambda expressions are one line functions without a name. However, we can assign the function to a variable to give it a name. They are
just needed where they have been created i.e when we don’t want to use a function twice. Lambda functions are mainly used in combination
with the functions filter(), map() and reduce(). This function can have any number of arguments and only one expression, which is
evaluated and returned. They aren’t capable of multiple expressions and can only handle single expressions. The format of lambda
statements is as follows:

Syntax: function_name = lambda <arguments> : <expression>

arguments is the inputs to be passed to the function[Required]
expression is applied on all the elements passed to the function[Required]
Example:

The following example of a lambda function returns the sum of its two arguments:

add = lambda x, y: x + y
print(add(5, 5))
#Output:
10
Useful use cases in list:

List sorting

#List sorting based on second value
car_list = [(4, 'Chevrolet'), (8, 'Audi'), (6, 'Hyundai'), (12, 'Toyota'), (9, 'Mercedes-Benz')]
car_list.sort(key=lambda x: x[1])
print(car_list)
#Output:
[(8, 'Audi'), (4, 'Chevrolet'), (6, 'Hyundai'), (9, 'Mercedes-Benz'), (12, 'Toyota')]
Joined by space

word_list = ['she', 'sell', 'seashell', 'on','the','seashore']
sentence = lambda x : ' '.join(x)
print(sentence(word_list))
#Output:
she sell seashell on the seashore
This will create a function called sentence and will return a string with each item of the list separated by a space.

6. Control Structures : Map, Filter, and Reduce
Map
Map is a function that works like list comprehensions and for loops. It is used when we need to map or implement functions on all
the items in the sequence at the same time. It returns a new list with the elements changed by <function>.

Syntax: map((<function> , <sequence>)

function is applied on all the items in the sequence at the same time[Required]
sequence is the iterable (can be list , set or dictionaries) [Required]
Example:

Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:

#Using for loop
num_list = [1, 2, 3, 4, 5]
square_list = []
for i in num_list:
    square_list.append(i**2)
print(square_list)
#output
[1, 4, 9, 16, 25]
Map allows us to implement this in a much simpler and nicer way. Also, the advantage of the lambda operator can be seen when it is used
in combination with the map() function.

#using map and lambda
num_list = [1, 2, 3, 4, 5]
square_list = list(map(lambda x: x**2, num_list))
print(square_list)
#output
[1, 4, 9, 16, 25]
map() can be applied to more than one list. The lists have to have the same length.

#using two lists
num_list1 = [3,5,9,7]
num_list2 = [4,5,6,7]
print(list(map(lambda x,y : x+y, num_list1,num_list2)))
#output
[7, 10, 15, 14]
Filter
The filter resembles a for loop but it is a builtin function and faster. It requires the function to look for a condition and then,
only returns a list of elements from the collection that satisfy the condition.<function> returns a Boolean value, i.e. either True
or False.

Syntax: filter(<function> , <sequence>)

function is applied to filter elements based on the condition from the iterable (can be list , set or dictionaries) [Required]
sequence is the iterable (can be list , set or dictionaries) [Required]
Example:

#filter elements based on condition
fibonacci_series = [0,1,1,2,3,5,8,13,21,34,55]
odd_list = list(filter(lambda x: x % 2, fibonacci_series))
print(odd_list)
even_list = list(filter(lambda x: x % 2 == 0, fibonacci_series))
print(even_list)
#output
[1, 1, 3, 5, 13, 21, 55]
[0, 2, 8, 34]
Reduce
Reduce is an operation that breaks down the entire process into pair-wise operations and uses the result from each operation, with
the successive element i.e a rolling computation to sequential pairs of values in a list.It returns a single value.

Syntax: reduce(<function> , <sequence>)

function is applied cumulatively to the item of the iterable to reduce it to single value(can be list , set or dictionaries) [Required]
sequence is the iterable (can be list , set or dictionaries) [Required]
Example:

#product of a list of integers using for loop
num_list = [2, 5, 3, 1, 4]
product = 1
for num in num_list:
    product = product*num
print(product)
#Output
120
#using reduce
from functools import reduce
product = reduce(lambda x,y: x*y, num_list)
print(product)
#Output
120
#Determining the maximum of a list of numerical values by using reduce
max_value = lambda x,y: x if (x > y) else y
reduce(max_value, num_list)
#Output
5
Conclusion
These were some of the useful built-in list methods and functions in Python. Along with that we also learnt about various other
useful operations that can be performed on the list such as list comprehension, slicing, indexing etc. There are other features
and operations which are not mentioned in the article but are equally important. We can refer Python documentation for deeper
insight.


'''