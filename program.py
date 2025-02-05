'''Question - You are given an array of integers called nums. Your task is to create a new array
 result such that each element at index i of the result is the product of all the elements in
  nums except nums[i].

nums - [1,2,3,4]
result-[24,12,8,6]
'''
'''
# Function to print a half pyramid pattern
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("A ", end="")
        print("")

# Example: Print a half pyramid with 5 rows
n = 5
half_pyramid(n)
'''