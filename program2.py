'''Question - You are given an array of integers called nums. Your task is to create a new array
 result such that each element at index i of the result is the product of all the elements in
  nums except nums[i].

nums - [1,2,3,4]
result-[24,12,8,6]
'''


def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Left product (product of elements before the current index)
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Right product (product of elements after the current index)
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example usage
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)
