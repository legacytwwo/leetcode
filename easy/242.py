def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    unique_letters = set(s)

    for letter in unique_letters:
        if s.count(letter) != t.count(letter):
            return False
    
    return True


assert isAnagram(s='anagram', t='nagaram') == True
assert isAnagram(s='angel', t='glean') == True
assert isAnagram(s='brag', t='grab') == True
assert isAnagram(s='rat', t='car') == False
assert isAnagram(s='city', t='lake') == False
assert isAnagram(s='cat', t='mobile') == False