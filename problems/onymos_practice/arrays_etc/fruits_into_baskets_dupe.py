# REVIEW LATER

# Doing this again for review
# 904. Fruit Into Baskets
# Medium
# https://leetcode.com/problems/fruit-into-baskets/description/

# You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. 
# However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit.
#   There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, 
#   you must pick exactly one fruit from every tree (including the start tree) 
#   while moving to the right. 
#   The picked fruits must fit in one of your baskets.

# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2: return len(fruits)
        max_fruits = 0
        
        left, right = 0, 1
        tracker = Counter()
        tracker[fruits[left]] = 1

        while right < len(fruits):
            # current_array = fruits[left: right +1]
            val_left, val_right = fruits[left], fruits[right]
            tracker[val_right] += 1

            while len(tracker) > 2:
                tracker[fruits[left]] -= 1
                if tracker[fruits[left]] == 0:
                    del tracker[fruits[left]]
                left += 1
                # current_array = fruits[left: right +1]

 
            max_fruits = max(right - left + 1, max_fruits)
            right +=1


        return max_fruits
    
# PLAN:
# TIme: O(n) one pass
# Space: O(1)
# Need: Dict to track numbers of fruits

# max_fruits = 0
# if len(fruits) == 0 return 1

# left, right = 0, 1
# tracker = default dict int, num fruits per type of fruit

# while right < len(fruits):
    # val_left, val_ right = fruits[left], fruits[right]
    # counter[val_right] ++
    # if val right not in tracker: # we have three types of fruit
        # while tracker[val_left] > 0:
            # left++ 
            # tracker[left] --

    # max fruits = max (counter[val_right] + counter[fruits[left]])

    # right++


# return max_fruits

solution = Solution()
print(solution.totalFruit([1,2,1])) # 3
print(solution.totalFruit([0,1,2,2])) # 3
print(solution.totalFruit([1,2,3,2,2])) # 4