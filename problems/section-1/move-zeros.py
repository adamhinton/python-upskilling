# Write an algorithm that takes an array
#  and moves all of the zeros to the end, 
# preserving the order of the other elements.

from typing import List

def move_zeros(lst: List[int]) -> List[int]:

    solution: List[int] = []
    num_zeros = 0

    for num in lst:
        if num == 0:
            num_zeros += 1
        
        else:
            solution.append(num)

    solution.extend([0] * num_zeros)

    return solution

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]

# PLAN:

# First concern is time complexity
# Don't want to mutate array in place - 
    # That's a lot of unnecessary O(n) ops
# Can do this in one pass I believe

    # solution: List[int] = []
    # num_zeros = 0

    # for num in lst:
        # If != 0, add num to solution

        # If == 0, num_zeros++

    # Make an array of zeros of length num_zeros
    # Add that array to solution (solution = solution + zeros_list)
    # Return solution