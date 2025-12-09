from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        mono_stack = []

        for idx in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[idx]
            while mono_stack and temperatures[mono_stack[-1]] <= temp:
                mono_stack.pop()

            solution[idx] = 0 if not mono_stack else (mono_stack[-1] - idx)

            mono_stack.append(idx)

        return solution

my_solution = Solution()
print(my_solution.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(my_solution.dailyTemperatures([30,40,50,60])) # [1,1,1,0]
print(my_solution.dailyTemperatures([30,60,90])) # [1,1,0]
