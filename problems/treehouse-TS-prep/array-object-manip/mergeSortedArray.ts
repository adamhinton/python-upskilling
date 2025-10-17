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
// Want O(m+n)

// We want to start at the end of both arrays (aka highest number in both)
// Tack whichever is highest on to end of nums1
// Repeat until we've finished off both arrays

function merge(nums1: number[], m: number, nums2: number[], n: number): void {

    let last = m + n - 1;

    while(m > 0 && n > 0){
        // nums1's element is bigger
        if(nums1[m] > nums2[n]){
            nums1[last] = nums1[m]
            m--
            last--
        }
        
        // Nums2's element is bigger or the smae
        else{
            nums1[last] = nums2[n]
            n--
            last--
        }
    }

    // We've arrived at the end of nums1's length 

};

console.log(merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)) // [1,2,2,3,5,6]