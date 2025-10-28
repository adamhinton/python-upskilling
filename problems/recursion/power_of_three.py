# https://leetcode.com/problems/power-of-two/description/

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# PLAN:

# Recursion
# Should be O(log3(n))

# if n== 0 return false

# if n%3 === 0 and isPowerOfThree(n/3) return true

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        return (n%3 == 0 and (n==3 or self.isPowerOfThree(n/3))) or n== 1
    
solution = Solution()


print("Should be true", solution.isPowerOfThree(27))
print("Should be false", solution.isPowerOfThree(0))