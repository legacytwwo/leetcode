def search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    mid = 0
    
    while low <= high:

        mid = (high + low) // 2

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    
    return -1


assert search([-1,0,3,5,9,12], 9) == 4
assert search([-1,0,3,5,9,12], 2) == -1