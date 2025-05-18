from typing import List

def max_profit(prices: List[int]) -> int:
    buy_pointer = 0
    sell_pointer = 1

    lowest_buy_price = prices[0]
    highest_sell_price = prices[1]

    prices_len = len(prices)

    # Don't think I need to include check on buy_pointer here
    while sell_pointer < prices_len:
        current_buy_price = prices[buy_pointer]
        current_sell_price = prices[sell_pointer]

        # Sell_pointer stuff
        if current_sell_price > highest_sell_price:
            highest_sell_price = current_sell_price
        
        # I think I can increment it on every loop? Not doing it this time
        # Right now this doesn't change sell_pointer if it's currently the best oen
        elif sell_pointer < prices_len:
            sell_pointer += 1
        

        if current_buy_price < lowest_buy_price:
            lowest_buy_price = current_buy_price
        
        # Doesn't change buy_pointer if it's currently the best one
        elif buy_pointer < (sell_pointer - 1):
            buy_pointer += 1

    return highest_sell_price - lowest_buy_price

print(max_profit([3, 10, 8, 4])) # 7

# PLAN:

# Two pointers starting at index 0 and 1
# buy can never be equal to or greater than sell
# buy_pointer = 0
# sell_pointer = 1

# lowest_buy_price = 0
# highest_sell_price = 0

# prices_len = len(prices)

# while sell_pointer < prices_len AND buy_pointer < (prices_len - 1):
    # current_buy_price = prices[buy_pointer]
    # current_sell_price = prices[sell_pointer]

    # if current_sell_price > highest_sell_price:
        # highest_sell_price = current_sell_price
    # Doesn't change sell_pointer if it's currently the best one
    # elif sell_pointer < prices_len:
        # sell_pointer++

    # if current_buy_price < lowest_buy_price:
        # lowest_buy_price = current_buy_price
    # Doesn't change buy_pointer if it's currently the best one
    # elif buy_pointer < (sell_pointer < 1):
        # buy_pointer++

# return highest_sell_price - lowest_buy_price



# Description:
# You're a buyer/seller and your buisness is at stake... You need to make profit... Or at least, you need to lose the least amount of money!
# Knowing a list of prices for buy/sell operations, you need to pick two of them. Buy/sell market is evolving across time and the list represent this evolution. First, you need to buy one item, then sell it later. Find the best profit you can do.

# Example:
# Given an array of prices [3, 10, 8, 4], the best profit you could make would be 7 because you buy at 3 first, then sell at 10.

# Input:
# A list of prices (integers), of length 2 or more.

# Output:
# The result of the best buy/sell operation, as an integer.

# Note:
# Be aware you'll face lists with several thousands of elements, so think about performance.