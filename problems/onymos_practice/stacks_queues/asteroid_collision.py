# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

# We are given an array asteroids of integers representing asteroids in a row.
# The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        solution = [] # stack

        for ast in asteroids:
            if not solution or ast > 0:
                solution.append(ast)
                continue

            while solution and solution[-1] > 0:
                if abs(ast) > abs(solution[-1]):
                    solution.pop() # # top of stack explodes, move on to next asteroid in stack

                elif abs(ast) < abs(solution[-1]):
                    continue # ast explodes

                else: # the're equal
                    solution.pop()
                    break # they both explode



        return solution
    
# PLAN
# O(n), one pass
# Need: Stack

# Make a stack. Positive asteroids move up the stack towards the top,
# negative asteroids move down the stack towards the bottom.
# Could also move the opposite way but I find this more intuitive.

# NOTES:
    # Asteroids' values will never initially be 0

# for ast in asteroids:
    # if not solution, add ast to solution
        # Continue

    # if ast is positive:
        # solution.append(ast)
        # continue

    # If ast is negative:
        # while the top asteroid is positive:
            # if abs(ast) > abs(top_ast):
                # solution.pop() # top asteroid explodes from stack
            # elif abs(ast) < abs(top_ast):
                # ast explodes; just continue
            # else: >>> they're equal and annihilate each other
                # solution.pop()
                # continue

# return solution

solution = Solution()
print(solution.asteroidCollision([5,10,-5])) # [5, 10]
print(solution.asteroidCollision([8,-8])) # []
print(solution.asteroidCollision([10,2,-5])) # [10]

