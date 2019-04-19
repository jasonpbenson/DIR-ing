# Friday, April 19

# Whiteboarding/Psuedocoding/talking through a problem/explaining your code/
# coming up with solutions together!

# Remember, we're all at different experience levels, so start with a couple of the 
# "warm up" problems so everyone can participate; don't just jump on the last 3! :D

# TRY to stay away from built-in methods like count() sort() replace() ord() etc, for now...

# 1
# write a function that counts the appearance of a letter within a string.
# casing should NOT matter.

# single_letter_count("Hello World", "h") # 1
# single_letter_count("Hello World", "z") # 0
# single_letter_count("HelLo World", "l") # 3

#define single_letter_count below:
def single_letter_count(string, letter):
    pass

# 2
# this function takes in a string and returns a dictionary with letters and
# their count in the string.
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

# flesh out multiple_letter count:

def multiple_letter_count(str):
    pass

# challenge: count vowels only!, or try a sentence and discount spaces

# 3
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
# so "a" is considered a different type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# feel free to change these variables below
j = 'aA'
s = 'aAAbbbb'

def num_jewels_in_stones(jewels, stones):
    pass


# 4
# write a function that accepts a string and tests if it is a palindrome
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True

def is_palindrome(str):
    pass


# 5
# write a function that accepts a list and a search term and returns the number
# of times the search term appears in the list
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1

def frequency(list, letter):
    pass 


# 6
# write a function that accepts a list of numbers and returns the product of all
# even numbers of list
# multiply_even_numbers([2,3,4,5,6]) # 48

def multiply_even_numbers(list):
    pass


# 7
# write a function that accepts a string and returns the same string with the
# first letter capitalized. perhaps use slices to help you out! DON'T use .capitalize()
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"

def capitalize(string):
    pass


# 8
# total sum of all numbers divisible by 3 or 5 < 1000

def sum_odds_by_three_five(int):
    pass


# 9
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def sum_even_fib():
    pass


# 10
# Write a function called average_pair. given a list of SORTED (ie: 1,2,3) integers and a target avg, 
# determine if there is a pair of values in the array where the average of the pair equals the target avg.
# There may be more than one pair that matched the target avg.

# examples:
# average_pair([1,2,3]. 2.5) returns TRUE
# average_pair([-1,0,3,4,5,6], 4.1) returns FALSE

def average_pair(list, avg):
    pass


# 11
# Write a function which returns a generator that will yield and unlimited number of primes, 
# starting from the first prime, which is 2
# primes = next_prime()
# [next(primes) for i in range(25)]
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def next_prime():
    pass


# ======================================= SOLUTIONS =============================================


# SINGLE LETTER COUNT --------------------------------->
# def single_letter_count(string, letter):
#     letter_count = 0
#     for char in string.lower():
#         if char == letter:
#             letter_count += 1
#     return letter_count

# print(single_letter_count('alOha amigo it is so sunny today', 'o'))

# def single_letter_count(string, letter):
#     return string.lower().count(letter.lower())


# MULTIPLE LETTER COUNT --------------------------------->
# def multiple_letter_count(str):
#     letter_counter = {}
#     for letter in str:
#         if letter != " ":
#             if letter not in letter_counter:
#                 letter_counter[letter] = 1
#             else:
#                 letter_counter[letter] += 1
#     return letter_counter

# print(multiple_letter_count('spaghetti and meatballs'))

# def multiple_letter_count(string):
#     return {letter: string.count(letter) for letter in string}


# JEWELS & STONES --------------------------------->
# def num_jewels_in_stones(jewels, stones):
#     jewelCount = 0
#     for letter in stones:
#         if letter in jewels:
#             jewelCount += 1
#     return jewelCount

# print(num_jewels_in_stones(j, s))


# IS PALINDROME --------------------------------->
# test_string = input('type any word: ')
# def is_palindrome(str):
#     if str[::1] == str[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome(test_string))
# print(is_palindrome('jason'))

# ----

# input_string = input("enter a word: ")
# def low_case(c):
#     return c.lower()

# def is_palindrome(str):
#     lower_input_string = low_case(str)
#     start = 0
#     end = len(lower_input_string)-1
#     while start < end:
#         if str[start] != str[end]:
#             return False
#         elif str[start] == str[end]:
#             start += 1
#             end -= 1
#     return True


# print(is_palindrome(input_string))


# FREQUENCY --------------------------------->
# def frequency(list, letter):
#     count = 0
#     for char in list:
#         if char == letter:
#             count += 1
#     return count

# print(frequency(['b', 'u', 'm', 'b', 'l', 'e', 'b', 'e', 'e'], 'b'))

# def frequency(collection, searchTerm):
#     return collection.count(searchTerm)


# MULTIPLY EVENS --------------------------------->
# def multiply_even_numbers(list):
#     product = 1
#     for num in list:
#         if num % 2 == 0:
#             product *= num
#     return product

# print(multiply_even_numbers([2, 3, 4, 5]))


# CAPITALIZE --------------------------------->
# def capitalize(string):
#     cap_string = string[0].upper() + string[1::]
#     return cap_string

# print(capitalize('katie'))


# SUM ODDS  DIVISBLE BY 3 OR 5 --------------------------------->
# def sum_odds_by_three_five(num):
#     sum = 0
#     for i in range(0, num):
#         if i % 3 == 0 and i % 5 == 0:
#             sum += i
#     return sum

# print(sum_odds_by_three_five(1000))


# FIBONACCI SEQ < 4 MILLION --------------------------------->
# fib_seq = [1, 2]
# def sum_even_fib(arr, max):
#     sum = 0
#     running_total = 2
#     for i in arr:
#         if i < max:
#             sum = arr[-2] + arr[-1]
#             arr.append(sum)
#             if sum % 2 == 0:
#                 running_total += sum
#     return running_total

# print(sum_even_fib(fib_seq, 4000000))

## Connor's nicer solution:
# def sum_even_fib(max):
#     a = 1
#     b = 1
#     sum = 0
#     while a <= max:
#         if a % 2 == 0:
#             sum += a
#         a, b = b, a+b
#     return sum

# print(sum_even_fib(4000000))


# AVERAGE PAIRS --------------------------------->
# def average_pair(list, avg):
#     i = 0
#     j = len(list) - 1
#     while i < j:
#         average = (list[i] + list[j]) / 2
#         if average < avg:
#             i += 1
#         elif average > avg:
#             j -= 1
#         elif average == avg:
#             return True
#     return False

# print(average_pair([1,2,3,4,5,6,7,8,9], 4))


# NEXT PRIME GENERATOR --------------------------------->
# def next_prime():
#     num = 2
#     all_primes = set()
#     while True:
#         for prime in all_primes:
#             if num % prime == 0:
#                 break
#         else:
#             all_primes.add(num)
#             yield num
#         num += num % 2 + 1
