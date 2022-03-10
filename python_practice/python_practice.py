x = 3


type('Hello!')


my_items = ['glasses', 'purse', 'cat']

my_items[0]

my_numbers = range(2, 10)

my_numbers[4]

list(my_numbers)


things = ['Apple', 'Grape', 101, 'Onion', False]

things[0]
# extracting the first element of the list

things[-1]
# extracting the last element of the list

things[0:4]
# extracting everything but the last

# finding the type of the 3rd, 4th, and 5th element
type(things[2])
type(things[3])
type(things[4])

# creating a list of 11,12,13,14,15 using range()

my_range = range(11, 16)
list(my_range)

numbers = [4, 19, 5, 94, 2]

numbers.sort()
numbers

numbers.remove(5)
numbers

numbers.append(55)
numbers


primes = [1, 2, 3, 5, 7]

# removing number 1
primes.remove(1)
primes

# add 11, 13, 17
primes.extend([11, 13, 17])
primes

primes.reverse()
primes

animal = 'chicken'

if animal == 'chicken':
    print('My favourite animal!')
else:
    print('Sad, not my favourite')

numbers = [1, 2, 3, 4]

numbers_squared = [number * number for number in numbers]
numbers_squared

# determine age based on year

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991, 1976, 1984, 1940]
age = [2022 - year for year in years_of_birth]
age

def is_palindrome(input_string):
        reversed_string = ''.join(reversed(input_string))
        if input_string == reversed_string:
            return True
        else:
            return False

# Write a function is_palindrome(input_string) to determine whether an input string is a palindrome
# (i.e. reads the same backwards as forwards, e.g. 'madam').
# The function should return True if the string is a palindrome and False otherwise.
# As an extension, amend your code so that it strips out spaces from the string.
# [Hint - to do this efficiently, research methods to reverse a string in Python]

# this function worked - checked in Anaconda.

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# number_range = range(1, 10)

#for number in number_range:
#    if(number % 3 == 0):
#        print(number)
#    elif(number % 5 == 0):
#        print(number)
#    else:
#        number_range.pop()


# Sidestep - trying to figure out indentation and loops in python

def greet():
    print('Hey!')

greet()
# this works. 

def calculate_mean(x, y):
    sum = x + y
    return sum

calculate_mean(5, 6)





def is_even(number):
	if(number % 2 == 0):
		return True
	else:
		return False

def sum_of_even_numbers(numbers):
	running_total = 0
	for number in numbers:
		if(is_even(number)):
			running_total += number
	return running_total
