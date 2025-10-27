# Another fairly easy one, just staying sharp
# This will be a good way to practice using the debugger in recursion, which I haven't really done before.

# https://leetcode.com/problems/fibonacci-number/description/

# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

# 0 <= n <= 30


class Solution:
    def fib(self, n: int) -> int:

        if n==0 or n==1: return n
        
        return 0
    

# PLAN:
# Recursion

# If n=0 or n==1, return n

# running_sum = 1
# numbers = [0, 1]
# current_index = 1

# while current_index < n:
    # num_to_add = numbers[current_index - 1] + numbers[current_index - 2]

    # running_sum += num_to_add

    # numbers[n] = running_sum

    # return running_sum + fib(curr_index+1)

solution = Solution()
print("should be 1:", solution.fib(2))  # 1
print("should be 2:", solution.fib(3))  # 2
print("should be 3:", solution.fib(4))  # 3