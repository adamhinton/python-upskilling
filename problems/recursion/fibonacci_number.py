# Another fairly easy one, just staying sharp
# This will be a good way to practice using the debugger in recursion, which I haven't really done before.

# https://leetcode.com/problems/fibonacci-number/description/

# 509. Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        
        return 0
    

# print examples with n=2, n=3 and n=4; comment the expected solution at end of line

solution = Solution()
print("should be 1:", solution.fib(2))  # 1
print("should be 2:", solution.fib(3))  # 2
print("should be 3:", solution.fib(4))  # 3