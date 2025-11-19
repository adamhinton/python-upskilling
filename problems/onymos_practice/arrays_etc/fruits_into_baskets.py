# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/
# Medium

# You are visiting a farm that has a single row of fruit trees arranged from left to right. 
# The trees are represented by an integer array fruits 
#   where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. 
# However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. 
#   There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, 
#   you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
#   The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2: return len(fruits)

        max_fruits = 0
        left, right = 0, 1

        return max_fruits
    
# PLAN
# Time: O(n)
# Space: O(n)
# Need:
    # Two pointers sliding window
    # Hash map

# if fruits is length 1 or 2, return len(fruits)

# max_fruits = 0
# left, right = 0, 1
# tracker = defaultdict(int)

# first_val = fruits[left] # first fruit type
# second_val = fruits[right] # second fruit type

# while right < len(fruits): # left should never come to equal right
    # new_val = fruits[right]
    # increment tracker for new val
    # if new_val != first val and != second val:
        # left++ until no more instances of first_val;
            # decrementing tracker[first_val] every time
        # right val = new val
        # left val = old right val

    # now we know it's a valid set
    # current_max_fruits = tracker[left val] + tracker[right val]

    # max_fruits = max(current max and max_fruits)
    # right++


# return max_fruits

solution = Solution()
print(solution.totalFruit([1,2,1])) # 3
print(solution.totalFruit([0,1,2,2])) # 3
print(solution.totalFruit([1,2,3,2,2])) # 4