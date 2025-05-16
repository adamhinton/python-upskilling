# https://www.codewars.com/kata/537400e773076324ab000262/train/python

from typing import Dict, List, Tuple  # noqa: F401




def get_letter_number (letter: str) -> int:
    if len(letter) != 1:
        raise Exception("Length must be 1")

    index = ord(letter.lower()) - ord('a')
    return index

def group_anagrams(words: List[str]) -> List[List[str]]:
    solution = []
    seen: Dict[Tuple, List[str]] = {}

    for word in words:
        # 26 0's
        counts: List[int] = [0] * 26 

        for letter in word:
            letter_num = get_letter_number(letter)
            counts[letter_num] += 1

        key = tuple(counts)
        if key in seen:
            seen[key].append(word)
        else:
            seen[key] = [word]

    for arr in seen:
        solution.append(seen[arr])

    return solution

print(group_anagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]))


# Plan:

# get_letter_num:
    ## helper funciton to convert letter to its zero-indexed alphabetical order
    ## aka 'z' = 25; 'b' = 1

# solution = []
# seen: Dict[Tuple(26)] = {}

# for word in words:
    ## my_tuple = tuple(26) ----> fill with 0s
    ## for letter in word:
        ### index = get_letter_num(letter)
        ### my_tuple[index] += 1
    ## Tuple is now done
    ## if seen[tuple], seen[tuple] += 1
    ## else seen[tuple] = [word]

# for item in seen:
    ## solution.append(seen[item])