# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

# Instructions are too long to copy here, but basically:
# Take string input
# Return first character that only appears in the string once
# Upper and lowercase chars are considered the same character, but fn...
    # ... should return the correct case for initial letter
# Edge cases:
    # If all characters repeat, return ""

from typing import Dict

def first_non_repeating_letter(input: str) -> str:
    frequency_counter: Dict[str, int] = {}

    for char in input:
        if frequency_counter.get(char):
            frequency_counter[char] += 1
        
        else:
            frequency_counter[char] = 1
    
    for char, count in frequency_counter.items():

        lower = char.lower()
        upper = char.upper()


        if lower == upper:
            total = frequency_counter.get(char)
        
        else:
            total = frequency_counter.get(upper, 0) + frequency_counter.get(lower, 0)
        
        if total == 1:
            return char
    
    return ""
        


print(first_non_repeating_letter('a')) # 'a'
print(first_non_repeating_letter('moonmesn')) # 'e'
print(first_non_repeating_letter('')) # ''
print(first_non_repeating_letter('abba')) # ''
print(first_non_repeating_letter('~><#~><')) # '#'
print(first_non_repeating_letter('hello world, eh?')) # 'w'
print(first_non_repeating_letter('sTreSS')) # 'T'
# PLAN
# note: Need to account for capitalization

    # note, don't need to explicitly check for zero-length input string

    # frequency_counter: Dict[str, int]= {}

    # for char in input:
        # if char is in frequency_counter, frequency_counter[char] += 1
        # else, frequency_counter[char] = 1

    # Note, dicts preserve insertion order now
    # for key, value in loop over frequency_counter.keys():
        # If value = 1 and key.upper() isn't in frequency_counter: 
            #  return key

    # No non-repeating characters
    # return ""
