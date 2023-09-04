from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    length = len(nums)
    products = [1] * length
    for i in range(1, length):
        products[i] = products[i-1] * nums[i-1]
    right = nums[-1]
    for i in range(length-2, -1, -1):
        products[i] *= right
        right *= nums[i]
    return products


assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
assert productExceptSelf([9,1,8,10]) == [80,720,90,72]