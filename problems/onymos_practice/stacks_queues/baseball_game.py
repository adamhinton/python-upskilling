# 682. Baseball Game

# The rules for this are long; please see here:
# https://leetcode.com/problems/baseball-game/description/

from typing import List
from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = deque([])

        for op in operations:
            if op == "+":
                new_score = scores[-1] + scores[-2]
                scores.append(new_score)

            elif op == "D":
                new_score = 2 * scores[-1]
                scores.append(new_score)

            elif op == "C":
                scores.pop()

            else: # it's an integer
                scores.append(int(op))
        
        return sum(scores)
    
# PLAN:
# O(n)
# NEED: Deque stack
# Think I could probably do this without iterating over my list of scores again; 
#   might try that after I get a working solution

# Notes:
# all operations are valid; don't need to validate them

# scores = deque([])

# for op in operations:
    # Number:
    # if op can be converted to a number, add op to scores

    # "+"
    # scores.append(last score plus second to last score)

    # "D"
    # scores.append(2 * scores[-1])

    # "C"
    # scores.pop()

# return sum(scores)

solution = Solution()

print(solution.calPoints(["5","2","C","D","+"])) # 30
print(solution.calPoints(["5","-2","4","C","D","9","+","+"])) # 27
print(solution.calPoints(["1","C"])) # 0