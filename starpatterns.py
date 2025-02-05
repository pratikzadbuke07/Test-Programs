
'''    

n=5
for i in range(n):                         
    print(''*(i*2),end='')
    for j  in range(n-i):
        print('*',end='')
    print()
print('================================================')    

n=5
for i in range(n):
    print(' '*i,end='')
    for j  in range(n-i):
        print('*',end='')
    print()

print('================================================')    

  
    
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
    
print('================================================')    
    
nrows=5
ncols=5

for i in range(nrows):
    for j in range(ncols):
        print('*',end='')
    print()
    
print('================================================')    

nrows=5
for i in range(1,nrows+1):
    print(' '*(nrows - i),end='')
    print(' * ' * i)
''' 
    
    
def func(num):
    n = 1
    while n <= num:
     yield n
    n = n + 1
    values = func(6)
    for i in values:
         print(i)