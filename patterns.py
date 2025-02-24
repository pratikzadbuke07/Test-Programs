# star pattern programs to print triangle
"""
*
* *
* * *
* * * *
* * * * * 
"""
s=int(input("enter a number:"))
for i in range(1,s+1):
    print("* "*i)
    i+=1

"""
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""

s=int(input("enter a number:"))
for i in range(1,s+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    i+=1


"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 """
def tri(n):
    num=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num+=1
        print()
        i+=1
tri(5)

s=int(input("enter a number :"))
p=1
for k in range(1,s+1):
    for j in range(1,k+1):
        print(p,end=" ")
        p+=1
    print()
    k+=1

"""
A 
B B 
C C C 
D D D D 
E E E E E 
"""

def alpha(n):
    p=65
    for i in range(n):
        for j in range(i+1):
            ch=chr(p)
            print(ch,end=" ")
        p+=1
        print()
alpha(5)

s=int(input("enter a number :"))
p=65
for i in range(1,s+1):
    for j in range(1,i+1):
        print(chr(p),end=" ")
    p+=1
    print()
    i+=1
"""
A A A A A 
B B B B 
C C C 
D D 
E 
"""


def apha(n):
    p=65
    for i in range(n):
        for j in range(i,n):
            ch=chr(p)
            print(ch,end=" ")
        p+=1
        print()
apha(5)

"""
          A 
        B B B 
      C C C C C 
    D D D D D D D 
  E E E E E E E E E 
"""

def apha(n):
    p=65
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print(chr(p),end=" ")
        for j in range(i):
            print(chr(p),end=" ")
        p+=1
        print()
    
apha(5)

"""
A 
B C 
D E F 
G H I J 
K L M N O 
"""
def apha(n):
    p=65
    for i in range(n):
        for j in range(i+1): 
            ch=chr(p)
            p+=1
            print(ch,end=" ")
        print()
apha(5)

n=int(input("enter a number :"))
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

""" 
A B C D E 
    F G H I 
      J K L 
        M N 
          O 
 """
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()


"""
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
* * * * * * * * *
"""
#hollow square pattern 
n=9
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


    #hollow hill pattern 
""" 
                  * 
                *   * 
              *       * 
            *           * 
          *               * 
        *                   * 
      *                       * 
    *                           * 
  * * * * * * * * * * * * * * * * *
 """


n=9
for i in range(n):
    for j in  range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if i==j or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
