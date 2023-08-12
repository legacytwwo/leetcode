def isValid(s: str) -> bool:

    if len(s) <= 1:
        return False

    stack = []
    brackets_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for bracket in s:
        if bracket in brackets_dict:
            stack.append(bracket)
        else:
            if not stack or brackets_dict[stack[-1]] != bracket:
                return False
            stack.pop()
    
    if stack:
        return False

    return True



assert isValid(s = "()") == True
assert isValid(s = "()[]{}") == True
assert isValid(s = "(]") == False
assert isValid(s = "(") == False
assert isValid(s = "{[]}") == True
assert isValid(s = "{[}]") == False
assert isValid(s = "({[]})") == True
assert isValid(s = "((") == False