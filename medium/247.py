from operator import itemgetter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    return [i[0] for i in sorted(counter.items(), key=itemgetter(1), reverse=True)[:k]]


assert topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2]
assert topKFrequent(nums = [1], k = 1) == [1]
assert topKFrequent(nums = [52, 11, 11, 13, 13, 13, 52, 1, 143, 11], k = 3) == [11, 13, 52]