from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    list_max = []
    deq = deque()

    for index, num in enumerate(nums):
        while deq and num > nums[deq[0]]:
            deq.pop()
        
        deq.append(index)

        if deq[0] == index-k:
            deq.popleft()

        if index >= k-1:
            list_max.append(nums[deq[0]])

    return list_max

assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert maxSlidingWindow([1], 1) == [1]