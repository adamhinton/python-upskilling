
# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction (positive meaning right, negative meaning left).
#  Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def is_same_direction(ast1: int, ast2: int) -> bool:
            return (ast1 < 0 and ast2 < 0) or (ast1 > 0 and ast2 > 0)

        solution = []

        for ast in asteroids:
            if (not solution) or solution[-1] <0 or ast > 0:
                solution.append(ast)
                continue

            # now we know ast is negative

            while solution[-1] > 0:

                top_asteroid = solution[-1]

                if abs(ast) > abs(top_asteroid):
                    solution.pop()
                    
                    if not solution or solution[-1] < 0:
                        solution.append(ast)
                        break
                    # continue    

                elif abs(ast) == abs(top_asteroid): # both explode
                    solution.pop()
                    break

                else: # ast is smaller
                    break

            

        return solution
    
# PLAN:
# O(n) time, O(n) memory
    # Could maybe make this O(1) memory by modifying asteroids in place and returning it
    # Edit: That might run in to weirdness with modifying an array while looping over it, nah
    # It's max 1000 asteroids, we don't have to worry about space

# Need:
    # monotonic stack

# Concept:
    # This simulation is like a literal physical stack:
    # heavier asteroids (negative ints) fall down
    # lighter asteroids (positive ints) rise up
    # Note that asteroids[i] != 0

# for ast in asteroids:
    # if not solution 
    # or if top ast is negative
    #  or ast is positive:
    #    add asteroid to solution

    # if ast is positive:
        # add ast to solution

    # if it's negative:
        # while top_asteroid is positive:
            # if abs(ast) > abs(top_asteroid):
                # solution.pop()
                # continue
                # if solution is None or new top_asteroid is negative:
                    # solution.append(ast)
                    # break
            # elif their abs values are equal:
                # solution.pop()
                # So, remove top asteroid from stack and don't add ast, they both exploded

            # elif abs(ast) < abs(top_asteroid):
                # break
                # Aka ast explodess

        

solution = Solution()
print(solution.asteroidCollision([5,10,-5])) # [5,10]
print(solution.asteroidCollision([8,-8])) # []
print(solution.asteroidCollision([10,2,-5])) # [10]
print(solution.asteroidCollision([3,5,-6,2,-1,4])) # [-6, 2, 4]
