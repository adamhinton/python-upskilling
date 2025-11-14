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
                # ast explodes; continue
            # else: >>> they're equal and annihilate each other
                # solution.pop()
                # continue
                
# return solution


