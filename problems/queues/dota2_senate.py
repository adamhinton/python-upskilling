# 649. Dota2 Senate
# https://leetcode.com/problems/dota2-senate/description/

# Problem description is too long to include here, but please see above link

# Notes: The runtime of this could be improved, especially when I make senate in to a deque. Can revisit this another time.
# Even despite this, my solution scored surprisingly well on runtime.

from typing import Literal
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> Literal["Dire", "Radiant"]:

        def opposite_party (senator: Literal["D", "R"]) -> Literal["D", "R"]:
            return "D" if senator == "R" else "R"

        senate_dq = deque([]) # will update this to be more efficient

        senator_numbers = {
            "D": 0,
            "R": 0,
        }

        for senator_char in senate:
            senator_numbers[senator_char] += 1
            senate_dq.append(senator_char)

        can_eliminate = {
            "R": 0,
            "D": 0
        }

        while True:
            senator_party = senate_dq.popleft()
            if can_eliminate[senator_party] > 0:
                can_eliminate[senator_party] -= 1
                senator_numbers[senator_party] -=1
            else:
                opposite = opposite_party(senator_party)
                can_eliminate[opposite] += 1
                senate_dq.append(senator_party)

            if senator_numbers[senator_party] == len(senate_dq):
                return "Dire" if senator_party == "D" else "Radiant"
                

solution = Solution()
print(solution.predictPartyVictory("RD")) # Radiant
print(solution.predictPartyVictory("RDD")) # Dire