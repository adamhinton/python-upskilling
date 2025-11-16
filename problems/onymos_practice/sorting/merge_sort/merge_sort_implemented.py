from typing import List

def merge_sort(arr: List[int]):
    if len(arr) > 1: # Base case
        left_arr = arr[:len(arr)//2] # beginning to midle point
        right_arr = arr[len(arr)//2:] # Middle point to end

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # index in merged array

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]: # left item is strictly smaller
                arr[k] = left_arr[i]
                i += 1

            else: # right item is smaller than left item, or they're equal
                arr[k] = right_arr[j]
                j += 1
            
            k +=1

        # Now deal with leftover items

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)

# Recursively:
    # Split array in half
        # Keep going until you get to just one item
    # Coming back up the recursion tree:
        # from left to right, compare a[left] to b[left] and so on
        # Add the lower item to solution first, then higher item
            # Or the other way around if it's descending order