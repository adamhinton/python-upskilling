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
    // {number: index}
    const numIndices: Record<number, number> = {}

    for(let i = 0; i< nums.length; i++){
        const num = nums[i]
        const needed = target - num
        if(needed in numIndices){
            return [i, numIndices[needed]]
        }

        numIndices[num] = i
    }

    // Should never happen if we do it right, always exactly one solution
    throw Error("Didn't find solution")
};

console.log(twoSum([2,7,11,15], 9)) // [0, 1]
// console.log(twoSum([3,2,4], 6)) // [1, 2]