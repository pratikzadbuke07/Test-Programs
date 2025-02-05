#self Keyword


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f" My name is {self.name} and my age is {self.age}")

d=Person("Nitin",39)        
d.info()
#=================================================================>

# args and kwargs
def sum(*args):
    total=0
    for i in args:
        total=total+i
    print("The  sum of all numbers is:",total)
sum(1,2,3,4,5)


def show(**kwargs):
    print(kwargs)
    
show(a=10,b=20,c=30)
