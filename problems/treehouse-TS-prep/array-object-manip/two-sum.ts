// https://leetcode.com/problems/two-sum/description/

// Given an array of integers nums and an integer target, 
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.

// You can return the answer in any order.

// PLAN:
// Make numIndexes object
// For num in nums,
    // needed = target - num
    // If needed in numIndexes, return those two indices
    // numIndexes[num] = i

function twoSum(nums: number[], target: number): [number, number] {
    
    return [-1, -1]
};