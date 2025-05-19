from typing import List

def max_profit(prices: List[int]) -> int:
    min_buying_price = prices[0]

    highest_possible_profit = prices[1] - min_buying_price

    # Start at prices[1] bc we can't sell for the price at index 0
    for price in prices[1:]:
        current_potential_profit = price - min_buying_price

        if current_potential_profit > highest_possible_profit:
            highest_possible_profit = current_potential_profit

        if price < min_buying_price:
            min_buying_price = price

    return highest_possible_profit

print(max_profit([3, 10, 8, 4])) # 7

# PLAN:

# min_buying_price = prices[0]
# highest_possible_profit = prices[1] - min_buying_price

# Start at prices[1] because you can't sell at prices[0]
# for price in prices[1::]:

    # current_potential_profit is price - min_buying_price
    # If that's greater than highest_possible_profit, then set highest_possible_profit = current_potential_profit

    # if price is lwoer than min_buying_price, min_buying_price = price

# return highest_possible_proit