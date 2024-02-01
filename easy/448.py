def findDisappearedNumbers(nums: list[int]) -> list[int]:
    progression = {i for i in range(1, len(nums)+1)}
    for i in nums:
        progression.discard(i)
    return list(progression)


assert findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
assert findDisappearedNumbers([1,1]) == [2]