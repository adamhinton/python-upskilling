# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).  # noqa: E501

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.  # noqa: E501


from typing import Dict, List, Tuple  # noqa: F401

# Do this for both ws:
# for letter in word:
## if letter not in freq:
### freq[letter] = 1
## else:
### freq[letter] +=1

# return freq1 deep equals freq2
## need to figure out how to do that


def is_anagram(w1: str, w2: str) -> bool:
    freq_1: Dict[str, int] = {}
    freq_2: Dict[str, int] = {}

    for letter in w1:
        letter = letter.lower()

        if letter not in freq_1:
            freq_1[letter] = 1
        else:
            freq_1[letter] += 1

    for letter in w2:
        letter = letter.lower()

        if letter not in freq_2:
            freq_2[letter] = 0
        freq_2[letter] += 1

    return freq_1 == freq_2


print(is_anagram("foefet", "toffee"))
print(is_anagram("foefdafaaet", "toffee"))
