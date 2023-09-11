def twoSum(numbers: list[int], target: int) -> list[int]:
    pointer1, pointer2 = 0, 1

    while numbers[pointer1] + numbers[pointer2] != target:
        if numbers[pointer1] + numbers[pointer2] < target:
            pointer1 += 1
            pointer2 += 1
        else:
            pointer1 -= 1
    return [pointer1+1, pointer2+1]


assert twoSum([2,7,11,15], 9) == [1,2]
assert twoSum([2,3,4], 6) == [1,3]
assert twoSum([-1,0], -1) == [1,2]
