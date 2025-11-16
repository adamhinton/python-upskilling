# Implementing this again for more practice

from typing import List

def merge_sort(arr: List[int]):
    """
    Modify in place, don't return anything
    """

    if len(arr) > 1: # Base case is len 1, do nothing if so
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[:len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        # Now left_arr and right_arr are sorted

        i = 0 # left index
        j = 0 # right index
        k = 0 # original array index, sorting in place

        while (i < len(left_arr) and (j < len(right_arr))):

            # I like naming these because it helps when running debugger
            left_element = left_arr[i]
            right_element = right_arr[j]

            if left_element < right_element: # left is strictly smaller
                arr[k] = left_element
                i += 1
            
            else: # right element is smaller or equal
                arr[k] = right_element
                j += 1

            k +=1

        # Now check leftovers
        while i < len(left_arr):
            left_element = left_arr[i]
            arr[k] = left_element
            i+= 1
            k += 1

        while j < len(right_arr):
            right_element = right_arr[j]
            arr[k] = right_element
            j += 1
            k += 1


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
