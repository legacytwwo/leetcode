def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    pointer = 0
    for i in range(len(t)):
        if t[i] == s[pointer]:
            pointer += 1
            if pointer == len(s):
                return True
    return False


assert isSubsequence(s="abc", t="ahbgdc") == True
assert isSubsequence(s="axc", t="ahbgdc") == False