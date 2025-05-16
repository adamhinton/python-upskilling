# https://www.codewars.com/kata/537400e773076324ab000262/train/python

from typing import Dict, List, Tuple  # noqa: F401

def group_anagrams(words: List[str]) -> List[List[str]]:
    solution = []

    for word in words:
        print(word)

    return solution

print(group_anagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]))