
#map function normal method 
def double(x):
    return x * 2
    
numbers=[1,2,3,4,5,6]

n=list(map(double,numbers))
print(n)

print("===============================================>")

#map function using lambda
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

print("===============================================>")

# filter function using normal method
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6,7,8,9,10,46486,67453,436755,363,41365]
even_numbers = list(filter(is_even, numbers))

print(even_numbers) 
print("===============================================>")

# filter function using lambda 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

print("===============================================>")
# reduce function using normal method
from functools import reduce
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)

print("===============================================>")
#reduce function using lambda function
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)







