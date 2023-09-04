from typing import List

def longestConsecutive(nums: List[int]) -> int:
    longest_cons = {}
    sorted_nums = sorted(set(nums))

    for num in sorted_nums:
        if num in longest_cons:
            longest_cons[num] += 1
            longest_cons[num+1] = longest_cons.pop(num)
        else:
            longest_cons[num+1] = 1
    return max(longest_cons.values()) if longest_cons else 0


assert longestConsecutive([]) == 0
assert longestConsecutive([0,0,-1]) == 2
assert longestConsecutive([100,4,200,1,3,2]) == 4
assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9