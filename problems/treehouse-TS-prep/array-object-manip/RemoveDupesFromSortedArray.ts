// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// 26. Remove Duplicates from Sorted Array

// Given an integer array nums sorted in non-decreasing order, 
// remove the duplicates in-place such that each unique element appears only once.
// The relative order of the elements should be kept the same. 
// Then return the number of unique elements in nums.

// Consider the number of unique elements of nums to be k, 
// to get accepted, you need to do the following things:

// Change the array nums such that the first k elements of nums 
//      contain the unique elements in the order they were present in nums initially. 
//      The remaining elements of nums are not important as well as the size of nums.
// Return k.

// PLAN
// O(n) I believe

// Need:
// Two pointers
// Just one pass I think
// Don't think I need a hash table

// If length is 0 or 1 return length

// let left, right = 0, 1

// while right < nums.length:
// numLeft, numRight = nums[left], nums[right]
// if numLeft === numRight, right++
// if numRight > numLeft:
    // nums[left + 1] = numRight
    // left ++?
    // right++?

// return left + 1



function removeDuplicates(nums: number[]): number {
    // if(nums.length < 2){
    //     return nums.length
    // }

    let left = 0
    let right = 1

    while (right < nums.length){
        const numLeft = nums[left]
        const numRight = nums[right]
        
        if(numRight === numLeft){
            right++
        }

        else if (numRight > numLeft){
            nums[left + 1] = numRight
            left++
            right++
        }

        else{
            throw Error("Left is greater than right. How did you even do that?")
        }

    }

    // console.log("nums", nums)

    return left + 1
};

// [1, 2, _], k=2
console.log(removeDuplicates([1,1,2]))
// [0,1,2,3,4,_,_,_,_,_] k = 5
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) 