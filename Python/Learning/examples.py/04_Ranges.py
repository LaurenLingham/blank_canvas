# You are creating a date picker for a website and need to output all of the years in a given period.
# Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
# The output sequence should start with the first input number and end with the second input number,
# without including it.

a = int(input())
b = int(input())
years = list(range(a,b))
print(years)