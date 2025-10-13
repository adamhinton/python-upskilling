// https://leetcode.com/problems/search-insert-position/description/

// Given a sorted array of distinct integers and a target value, 
// return the index if the target is found. 
// If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

// Plan: 
// Make two pointers low and high, 0 and last index
// Find middle of pointers
// while low <= high:
// mid = floor hi - low / 2
// if nums[mid] is target, return mid
// if target is greater, low = mid
// if target is lower, high = mid

// if doesn't exist, return where it would be - I think this is just the last remaining mid?

// if arr[mid] is target, return mid + 1

function searchInsert(nums: number[], target: number): number {
    let low = 0
    let high = nums.length - 1

    while (low <= high){
        const mid = Math.floor((low + high) /2)

        const currentNumber = nums[mid]

        if (target === currentNumber){
            return mid
        }

        if (target > currentNumber){
            low = mid + 1
        }

        else if (target < currentNumber){
            high = mid - 1
        }
    }

    return Math.floor((low + high) /2) + 1
};

console.log(searchInsert([1,3,5,6], 5)) // 2
console.log(searchInsert([1,3,5,6], 2)) // 1
console.log(searchInsert([1,3,5,6], 7)) // 4
