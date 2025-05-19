# Description:
# Write a function that takes a string of parentheses, 
# and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# Constraints:
# Input is only strings, with only ) and (
# Empty strings are valid and return True
# Input should not be mutated



from typing import Dict, List, Tuple  # noqa: F401

def valid_parentheses(paren_str: str) -> bool:
    balance = 0

    for paren in paren_str:
        if paren == "(": 
            balance += 1
        elif paren == ")": 
            balance -= 1

        if balance < 0: 
            return False
    
    return balance == 0

print(valid_parentheses("()")) # True
print(valid_parentheses(")(()))")) # False
print(valid_parentheses("(")) # False
print(valid_parentheses("(())((()())())")) # True


# PLAN:
# UPDATE: I ended up using a single counter.
# Create two variables:
# open_paren_count
# close_paren_count

# These two need to be equal at the end
# if close_paren_count is ever greater than open_paren_count, immediately return False

# So, for paren in paren_str:
    # if paren == "(" open_paren_count += 1
    # if paren == ")" close_paren_count += 1
    # If close_paren_count > open_paren_count return False

# At end:
    # return open == closed


# Optimization possibilities:
 # Some way to not check if closed is greater than open on every iteration? Probably not
 # While loop just does the same check