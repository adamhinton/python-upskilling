# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).  # noqa: E501

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.  # noqa: E501

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).  # noqa: E501

# Solution notes:
# I originally thought I'd have to loop over twice. But we got this down to O(n)
# Hashmaps are a godsend

from typing import Dict, List, Tuple


def two_sum(arr: List[int], sum_target: int) -> Tuple[int, int]:
    freq_dict: Dict[int, int] = {}

    for index, num in enumerate(arr):

        second_int_goal = sum_target - num

        if second_int_goal in freq_dict:
            return (index, freq_dict[second_int_goal])

        if num not in freq_dict:
            freq_dict[num] = index

    return (0, 0)


print(two_sum([1, 2, 3], 4))  # returns (0, 2) or (2, 0)
print(two_sum([3, 2, 4], 6))  # returns (1, 2) or (2, 1)
