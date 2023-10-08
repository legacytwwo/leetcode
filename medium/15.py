def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    sorted_nums = sorted(nums)
    len_nums = len(nums)
    for i in range(len(sorted_nums)):
        if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
            continue 
        
        j = i + 1
        k = len_nums - 1

        while j < k:
            pointers_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
            if pointers_sum > 0:
                k -= 1
            elif pointers_sum < 0:
                j += 1
            else:
                result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                j += 1
                while sorted_nums[j-1] == sorted_nums[j] and j < k:
                    j += 1 

    return result

assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert threeSum([0,1,1]) == []
assert threeSum([0,0,0]) == [[0,0,0]]