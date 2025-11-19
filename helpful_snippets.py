# DIRS = [(-1,0), (0,1), (1,0), (0,-1)]
# for a, b in DIRS:
#     x, y = row + a, col + b
#     if 0 <= x < m and 0 <= y < n and (other conditions here):
#          # call recursive_helper
            
# Stuff to try:
    # work backwards
        # start from right of array
        # Eliminate ineligible contenders first instead of finding eligible ones
            # e.g. in surroudned regions, eliminate ones who aren't surrounded first
    
    # modify arrays in place for tracking
    

# Backtracking:
    # Base case: When you get to the end
    # Start case: How the function is called

    # Branches: Which scenarios do you back track for?  
        # directions for mazes
        # Adding or not adding for permutations
        # etc


# Binary search:
def binary_search_template(arr, target):
    """
    Performs a binary search to find the first element in 'arr' that is 
    greater than or equal to 'target', or its insertion point.
    Assumes 'arr' is sorted in ascending order.
    """
    left, right = 0, len(arr) 
    # 'right' is initialized to len(arr) to represent the potential insertion point 
    # after the last element. The search space is [left, right).

    while left < right:
        mid = left + (right - left) // 2 
        # Calculate mid to prevent potential overflow with large left/right values.

        if arr[mid] < target:
            # If the middle element is less than the target, 
            # the target must be in the right half (or not present).
            # We discard mid and the left part, so move 'left' past 'mid'.
            left = mid + 1
        else:
            # If the middle element is greater than or equal to the target,
            # the target could be mid itself or in the left half.
            # We keep mid as a potential candidate, so move 'right' to 'mid'.
            right = mid

    # After the loop, 'left' (which equals 'right') will be the index of 
    # the first element greater than or equal to 'target',
    # or 'len(arr)' if all elements are less than 'target'.
    return left

# keywords: is_border_square, edge, outside, perimeter
# row == 0 or col == 0 or row == m-1 or col == n-1

# Outside squares
def get_outside_squares(rows, columns):
    """
    Enumerates all (row, column) coordinates on the outside of a grid.

    Args:
        rows (int): The number of rows in the grid.
        columns (int): The number of columns in the grid.

    Returns:
        list: A list of tuples representing the coordinates of the outside squares.
    """
    if rows <= 0 or columns <= 0:
        return []
    
    outside_squares = [
        (r, c)
        for r in range(rows)
        for c in range(columns)
        if r == 0 or r == rows - 1 or c == 0 or c == columns - 1
    ]
    return outside_squares

# Example outside squares usage
R = 4
C = 5
outside_coords = get_outside_squares(R, C)
print(f"Outside squares of a {R}x{C} grid:")
for coord in outside_coords:
    print(coord, end=" ")
print(f"\nTotal outside squares: {len(outside_coords)}")