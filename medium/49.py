def groupAnagrams(strs: list[str]) -> list[list[str]]:
    if not strs: return [[""]]
    anagrams = {}
    for word in strs:
        sorted_word = str(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


assert groupAnagrams(["anagram","nagaram"]) == [['anagram', 'nagaram']]
assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert groupAnagrams([]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]