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
        from collections import defaultdict

        left = 0
        counts = defaultdict(int)
        max_len = 0

        for right in range(len(fruits)):
            val = fruits[right]
            counts[val] += 1

            while len(counts) > 2:
                left_val = fruits[left]
                counts[left_val] -= 1
                if counts[left_val] == 0:
                    del counts[left_val]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
solution = Solution()
print(solution.totalFruit([1,2,1])) # 3
print(solution.totalFruit([0,1,2,2])) # 3
print(solution.totalFruit([1,2,3,2,2])) # 4
print(solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # 5
print(solution.totalFruit([0,0,1,1])) # 4
print(solution.totalFruit([1,0,1,4,1,4,1,2,3])) # 5