// https://leetcode.com/problems/merge-sorted-array/description/

// 88. Merge Sorted Array

// You are given two integer arrays nums1 and nums2, 
// sorted in non-decreasing order, 
// and two integers m and n, 
// representing the number of elements in nums1 and nums2 respectively.

// Merge nums1 and nums2 into a single array sorted in non-decreasing order.

// The final sorted array should not be returned by the function, 
// but instead be stored inside the array nums1. 
// To accommodate this, nums1 has a length of m + n, 
// where the first m elements denote the elements that should be merged, 
// and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

// PLAN:
// Generally, to loop backwards through nums1 and nums2, zipping them together as we go

// const i = m-1 >> position in nums1
// const j = n-1  >>> position in nums2
// const last = m + n - 1

// while i > 0 and j > 0
// if nums1[m] > nums2[n]
    // nums1[last] = nums1[m]
    // m--
// else
    // nums1[last] = nums2[n]
    // n--

// All remaning nums in nums2 are smaller so should go at the start
// while n > 0
    // nums1[last] = nums2[n-1]
    // n--
    // last--

// While i >=0 and j >=0:

function merge(nums1: number[], m: number, nums2: number[], n: number): void {

    let last = m + n - 1;
    let i = m - 1
    let j = n - 1

    while(i >= 0 && j >= 0){
        const nums1Num = nums1[i]
        const nums2Num = nums2[j]

        if(nums1Num > nums2Num){
            nums1[last] = nums1Num
            i--
            last--
        }
        else{
            nums1[last] = nums2Num
            j--
            last--
        }
    }

    while(j >= 0){
        nums1[last] = nums2[j]
        last--
        j--
    }

    // console.log("nums1:", nums1)
};

console.log(merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)) // [1,2,2,3,5,6]