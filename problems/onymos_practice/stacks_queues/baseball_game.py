# 682. Baseball Game

# The rules for this are long; please see here:
# https://leetcode.com/problems/baseball-game/description/

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        return 0
    
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
