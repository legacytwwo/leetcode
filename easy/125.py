def isPalindrome(s: str) -> bool:
    filtered_str = ''.join(letter for letter in s.lower() if letter.isalnum())
    if filtered_str == filtered_str[::-1]:
        return True
    return False


assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True
assert isPalindrome("r") == True
assert isPalindrome("ar") == False