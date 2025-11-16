# Implementing this again for more practice

from typing import List

def merge_sort(arr: List[int]):
    """
    Modify in place, don't return anything
    """

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)

# PLAN
# Time complexity: O(n log n)

# if len(arr) > 1:  >>> base case: get down to length 1
    # Divide in to left and right arrays
    # call merge_sort on left_array
    # call merge_sort on right array

    # i = 0 >> left index
    # j = 0 >> right index
    # k = 0 >> in original array 

    # while i < len(left_arr) and j < len (right_arr):
        # if left_arr[i] < right_array[j]:  # left element is smaller
            # arr[k] = left_arr[i]
            # i += 1
        
        # else: >> right element is smaller or equal
            # arr[k] = right_arr[j]
            # j += 1

        # k += 1

    # while i < len(left_arr):
        # arr[k] = left_arr[i]
        # i++
        # k++

    # while j < len(right_arr):
        # arr[k] = right_arr[j]
        # j++
        # k++
