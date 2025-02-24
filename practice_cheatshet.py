
def prime_no(n):
    Flag=True
    if n < 2:
        Flag = False
        return Flag
    else :
        for i in range(2,n):
            if n % i == 0:
                Flag = False
                break
    return Flag
                
num=int(input("enter a number:"))
prime_no(num)

print("################################################################")

def prime_no(n):
    Flag = True  # Assume the number is prime initially

    if n < 2:
        Flag = False
    else:
        for i in range(2, n):
            if n % i == 0:
                Flag = False  # Found a divisor, so it's not prime
                break  # No need to check further

    return Flag  # Return the final value of Flag

num = int(input("Enter a number: "))
print(prime_no(num))  # Print the result'''


print("################################################################")


# Palindrome string program 

string = "pratarp"
reversed_str = ""  # Initialize an empty string

for char in string:
    reversed_str = char + reversed_str  # Prepend each character

# Now you can use reversed_str in your palindrome check
if string == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")



print("################################################################")

#finding avarage of the tuples 
def avarage(*t):
    avg = sum(t)/len(t)
    return avg

result =  avarage(32,32,445,66,8943,45,66547,)
print("avarge is :",result)

print("################################################################")

class Test:
    def __init__(self):
        self.a=5
    def f1(self):
        self.b=10
t1=Test()
t2=Test()
t3=Test()
t1.f1()
t1.c=14
print(t1.__dict__)
print(t2.__dict__)
print(t3.__dict__)

#find factorial usng lambda function 
f = lambda n : 1 if n == 0 else n *f(n-1)
print(f(5))

print("################################################################")
# using logic


num = int(input("enter a number :"))
fact=1
if num<0:
    print("Factorial does not exist")
elif num == 0:
    
    print("Factial of 0 is 1")
else:
    for i in range(1,num + 1):
        fact=fact*i
    print(f"The fact of {num} is:",fact)

print("################################################################")
# list comprehensions 
list=[23,56,65,22,32,65,76,33,99]
l2=[i for i in list if i%2==0]
print(l2)

print("################################################################")

# split and join operations 
s = "my name is python and i love programming"

s1=s.split(" ")
print(s1)

s1=s1[::-1]
print(s1)
print(" ".join(s1))

print("################################################################")

# decorators 

def welcome(fun):
    def myfunc(*t,**d):
        print("before decorator this will run")
        fun(*t,**d)
        print("Thanks for Using My  Function")
    return myfunc
@welcome
def hello(): 
    print("HEllo !")

@welcome
def add(a,b):
    print(a+b)
    
hello()
add(1,3)

print("################################################################")

#class Decorator 
class Calculator:
    def __init__(self,func):
        self.function =  func
        
    def __call__(self,*t,**d):
        result = self.function(*t,**d)
        return result**2
@Calculator
def add(a,b):
    return a+b
print(add(10,20))


print("################################################################")


# marks problem using decoraators 

def  decor_results(result_function):
    def distinction(marks):
        result=[]
        for m in marks:
            if m>=75:
                print("Distinction")
        res=result_function(marks)
        result.append(res)
        return result
        
    return distinction
        
@decor_results
def result(marks):
    for m in  marks:
        if m>=33:
            pass
        else:
            print("fail")
            return  "fail"

    else:
        print("pass")
        return "pass"
        
result([45,78,80,34,66,90])
        
print("Results:",result) 

print("################################################################")


# itertators 
li=[1,2,3,4,5,6,7,88,8,65,3]
it=iter(li)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

print("################################################################")


#Usecase of yield key word 

def evenNum(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1
it= evenNum(10)
even_list=[]
while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break
print(even_list)

print("################################################################")


t1=(34,32,64,78,83,95,64)
s_t1=sorted(t1)
print(s_t1)
print(type(s_t1))

l1=[34,32,64,78,83,95,64]
l1.sort()
print(type(l1))
print(l1)

print("################################################################")


#Loops code 
i=1
while i<=10:
    print(i,end=" ")
    if i==5:
        break
    i+=1
    
else:
    print("You are in else statement")
    
print("##############################################")

for i in range(10):
    print(i,end=' ')
    if i==12:
        break
else:
    print("you aree in else statement")

# NAme mangling 
class world:
    x=10
    __india=20
    
print(world.x)
print(world._world__india)

class test:
    x=20
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,self.b)
        
print(test.x)
t1=test(4,5)
t1.show()

print(t1.a)
print(t1.b)

#init methiod
class test:
    def __init__(self):
        
        self.a=10
        self.b=20
    
t1=test()
print(t1.a,t1.b)

#default argument in function 

def add(a,b,c=5):
    return a+b+c
    
s= add(2,3)
print("The addition is:",s)

#extract int type values from hetrogenus elements
l1=['anbc',34.54,34,54,32,'b',66,'90']
print(l1)
l2=[]
for i in l1:
    if type(i)==int:
        l2.append(i)
print("the integrs are :",l2)

#Monkey patching 

class Test:
    def __init__(self,x):
        self.a=x
        
    def get_data(self):
        print("send the code to fetch data from database")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
        
t1=Test(5)
print(" before monkey patching code\n")
t1.f1()
t1.f2()

def get_new_data(self):
    print("some to code fetch data from test data")
    
Test.get_data = get_new_data
print("\n After monkey patching \n")
t1.f1()
t1.f2()

#prime or  not prime

num=int(input("enter a number:"))
for i in range(2,num):
    if num%i==0:
        print("number is not prime")
        break
    
else:
    print("number is prime")

#odd even code
num=int(input("enter a number:"))
if num%2==0:
    print(f"enterd {num} is even number")
else:
    print(f"enterd {num} is  odd  number")


#positive or negative number 

num=int(input("enter a number:"))
if num>0:
    print("number is postivre number")
elif num==0:
    print("number is zero")
else:
    print("number is negative ")
    
#sum of two numbers
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
print("num1+num2=",num1+num2)

# find GCD of two numbers

num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))

def gcd(a,b):
    if a==0 or a==b:
        return b
    elif b==0:
        return a
    elif a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
print(gcd(num1,num2))


