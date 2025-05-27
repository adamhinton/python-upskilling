# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

# Given a string s and an integer k, 
#   return the maximum number of vowel letters 
#   in any substring of s with length k.



class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        most_vowels = 0
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        current_vowel_count = 0

        left = 0
        right = k
        starting_substring = s[left: right]

        # Setting things up by checking starting window for vowels
        for char in starting_substring:
            if char in vowel_set:
                current_vowel_count += 1

            most_vowels = current_vowel_count

        first_char = starting_substring[0]
        if first_char in vowel_set:
            current_vowel_count -= 1

        left += 1
        right += 1


        while right < len(s):
            last_char = s[right-1]
            if last_char in vowel_set:
                current_vowel_count += 1
            
            most_vowels = max(most_vowels, current_vowel_count)

            first_char = s[left]
            if first_char in vowel_set:
                current_vowel_count -= 1

            left += 1
            right += 1
        

        return most_vowels

print(Solution().maxVowels(s="abciiidef", k=3))  # 3
print(Solution().maxVowels(s="aeiou", k=2))  # 2
print(Solution().maxVowels(s="leetcode", k=3))  # 2

# PLAN:

# most_vowels = 0
# vowel_set is a Set of aeiou
# current_vowel_count = 0

# left = 0
# right = k

# window = s[left, right]

# Loop over the first substring to set things up
# for char in starting_substring:
    # if char in vowel_set:
        # current_vowel_count += 1
    
    # most_vowels = current_vowel_count

    # right += 1
    # left += 1

# while right < k:
    # last_char = s[right]
    # if char is vowel, current_vowel_count++
    # update max vowel count if needed

    # first_char is s[left]
    # if first char is vowel, current_vowel_count --

    # left += 1
    # right -= 1


# return most_vowels



# Thoughts before planning:
# - Sliding window (obviously)
# -Should be O(n)
# not sure why this is LC medium; seems easy enough. Maybe I'll find hidden complications.
