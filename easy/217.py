def containsDuplicate(nums: list[int]) -> bool:
    return True if len(set(nums)) < len(nums) else False

assert containsDuplicate([1,2,3,1]) == True
assert containsDuplicate([1,2,3,4]) == False
assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True