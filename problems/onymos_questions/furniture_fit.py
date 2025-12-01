from typing import List
def fit(room_width: int, room_height: int, furniture_list: List, new_furniture) -> bool:
    # Bounds check - does it fit in the room alone?
    if new_furniture["x"] + new_furniture["w"] > room_width:
        return False
    if new_furniture["y"] + new_furniture["h"] > room_height:
        return False
    
    # Where it starts
    new_furniture_x = new_furniture["x"]
    new_furniture_y = new_furniture["y"]
    # Where it ends
    new_furniture_x_2 = new_furniture_x+ new_furniture["w"]
    new_furniture_y_2 = new_furniture_y + new_furniture["h"]

    # Overlap check against each existing furniture piece
    for f in furniture_list:
        # Where it starts
        fx1, fy1 = f["x"], f["y"]
        # Where it ends
        fx2, fy2 = fx1 + f["w"], fy1 + f["h"]

        # rectangles overlap: failure
        if not (
            (
                new_furniture_x_2 <= fx1
                or fx2 <= new_furniture_x
                or new_furniture_y_2 <= fy1
                or fy2 <= new_furniture_y
            )
        ):
            return False
        
    return True
            


    

# Plan:
# First, make sure the new piece can fit in the room at all
# If it's too wide or too tall, return false

# Then, make sure no other pieces overlap:
# For each piece in the room:
    # Calculate where it falls in the room
    # If those coordinates overlap with new piece, return False


# Notes:
# Treat every new furniture piece as an axis-aligned rectangle

# top leftcorner: (x, y)
# widdth: w
# height: w

# Furniture fits if:
# It stays inside room bounds
    # x >= 0
    # y >= o
# x2 = x + w
# y2 = y + w