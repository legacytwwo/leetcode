def lengthOfLongestSubstring(s: str) -> int:
    longest_sub = ''
    substring = ''
    for letter in s:
        if letter in substring:
            if len(substring) > len(longest_sub):
                longest_sub = substring
            substring = substring[substring.index(letter)+1:]
        substring += letter
    return max([len(longest_sub), len(substring)])

# Solving through sets should use less memory and time

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring(" ") == 1
assert lengthOfLongestSubstring("au") == 2
assert lengthOfLongestSubstring("dvdf") == 3