# Doing this again for practice

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
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2: return len(fruits)

        counter = Counter()
        max_fruits = 0
        left = 0
        right = 1
        counter[fruits[left]] = 1

        while right < len(fruits):
            right_val = fruits[right]

            counter[right_val] += 1

            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1


            current_max_fruits = sum(counter.values())
            max_fruits = max(current_max_fruits, max_fruits)

            right += 1

        return max_fruits
        

solution = Solution()
print(solution.totalFruit([1,2,1])) # 3
print(solution.totalFruit([0,1,2,2])) # 3
print(solution.totalFruit([1,2,3,2,2])) # 4
print(solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5
print(solution.totalFruit([0,0,1,1])) # 4
print(solution.totalFruit([1,0,1,4,1,4,1,2,3])) # 5