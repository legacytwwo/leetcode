def maxArea(height: list[int]) -> int:
    p1 = 0
    p2 = len(height) - 1
    max_value = min([height[p1], height[p2]]) * (p2 - p1)
    while p1 < p2:

        if height[p1] > height[p2]:
            p2 -= 1
        else:
            p1 += 1

        container = min([height[p1], height[p2]]) * (p2 - p1)

        if max_value < container: max_value = container
    return max_value
        

assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea([1,1]) == 1
assert maxArea([1,2,4,3]) == 4
        