'''
list1 = [3, 5, 4, 9, 8, 5, 7, 8, 12]

odd=[]
even=[]
j=0

for i in list1:
    if list1[j]%2==0:
        even.append(i)
    else:
        odd.append(i)
    j=j+1
    
print(even)
print(odd)
'''



#Print second largest element from the list

"""list = [20, 30, 40, 25, 10] 

val=list.sort()
print(val)
print(val[:-2])"""


"""list = [20, 30, 40, 25, 10] 
list.sort() 
print("The second large number :", list[-2]) """

"""arr = [1, 2, 3, 4, 5]
sum = 0
# Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
    sum = sum + arr[i]
print("Sum : " + str(sum))"""

#Bubble sort

"""
def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
array=[2,4,7,4,8,9,3]
bubble_sort(array)
print(array)"""

#reverse array

"""arr = [1, 2, 3, 4, 5];
for i in range(0, len(arr)):
    print(arr[i],end='')
print("\nreversal array: ");
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end='')"""

#Merge two  dictionaries
"""dict1={'a':10,'b':8}
dict2={'c':10,'d':8}
def merge(dict1,dict2):
    return(dict1.update(dict2))
merge(dict1,dict2)
print(dict1)

#another way through union opreator

dict1={'a':10,'b':8}
dict2={'c':10,'d':8}
print(dict(dict1 | dict2))"""


#12.int and string separation :-
"""a = "MH10CD7172"
num=""
word=""
for c in a:
    if c.isdigit():
        num = num + c
    else:
        word = word + c
print(num)
print(word)"""

#14.legnth of without space string
"""a = 'indexial solution is the best' 
print("string length with spaces is:"+str(len(a)))
result= sum(not chr.isspace() for chr in a)
print("string length without spaces is:"+str(result))"""

#Reverse list using recursion function
"""list1 = [1, 2, 3, 4, 5] 
def reverse_func(numbers):
    if len(numbers)==1:
        return numbers
    return reverse_func(numbers[1:])+numbers[0:1]
print(reverse_func(list1))"""
#to print even llength words in string 
"""n="this is pythonn language"
s=n.split("  ")
for i in s:
    if len(i)%2==0:
        print(i)"""

#addition of two list and output should be dict 
"""a=[3,4,5,6,78,9]
b=[1234,3456,56645,56656,4344,525]
ab={a[i]:b[i] for i in range(len(a))}
print(ab)
"""

#----------------------------------------------------------------------------------------------------------------
#to print the star pattern

"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""

#Capitalize first character in each word
"""list=["Hello","my","name","is","pratik"]

for i in range(len(list)):
    list[i]= list[i].capitalize()
print(list)

"""
#febonacii series

"""def fib(n):
    a=1
    b=0
    for i in range(n):
        print(b)
        a,b=b,b+a
fib(90)"""

#sum of all the elements in array 
# arr=[1,2,3,4,5,5,6,7]
# sum=0

# for i in range(0,len(arr)):
#     sum=sum+arr[i]
# print("sum: "+str(sum))

"""
num = 10

for i in range(num):
    for j in range(i):
        print(i*j,end=" ")
    print()
"""

#Find only tuple first element
"""a = [(3,4),(1,2),(5,6)]
c=sorted(a)
print(c)
b = [(x[0]) for x in c]
print(b)"""

#Reversing a numbers 
"""num=123
reversed_num=0

while num!=0:
    digit = num % 10
    reversed_num=reversed_num*10 +digit
    num //=10
print("Reversd Number:"+str(reversed_num))"""


#Nearest number of 0 :
"""def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: 
abs(lst[i]-K))] 
# Driver code
lst = [3,4,-8,3,2,-1,5]
K = 0
print(closest(lst, K)) """

#Print dict1 keys and dict2 values in one dictionary
"""dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}
output=(dict(zip(dict1.keys(),dict2.values())))
print(output)"""

# write a python progrsam to generate the random passwords of the given lengths 
"""import random
import string
def generate_password(length):
    password=''.join(random.choices(string.ascii_letters + string.digits,k=length))
    return password
print(generate_password(8))"""

#print vowels in the string 
"""
def count_vowels(string):
    vowels="aeiouAEIOU"
    count=0
    for ch in string:
        if ch in vowels:
            count +=1
    return count
print(count_vowels('Pankaj'))
"""

#write a Python program to find the sum of all the multiples of 3 or 5 in below numbers
'''
def sum_multiples(num):
    sum=0
    for i in range(num):
        if i % 3==0 or i % 5 ==0:
            sum += i
    return sum
print(sum_multiples(50))
'''
#2. find the unique characters in given string :
'''
a="bdbac353@#2c&191#"
unique_char=[]
for character in a:
    if character not in unique_char:
        unique_char.append(character.lower())
    else:
        unique_char.remove(character.lower())
print(format(unique_char))
'''
#Show only duplicates output in list
''' 
list = [10, 20, 30, 40, 50, 10, 20, 10]
new = [] 
for i in list:
    n = list.count(i)
    if n > 1:
        if new.count(i) == 0:
            new.append(i)
print(new)
'''
#3. insertion sort 
'''
n=[1,35,6,3,7,3,8,2,0]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]<n[j]:
            n[i],n[j]=n[j],n[i]
print(n)

'''
# input='the sky is blue'
# output='blue is sky the'

s='the sky is blue'
l= s.split()
print(l)
l=l[::-1]
l=" ".join(l)
print(l)