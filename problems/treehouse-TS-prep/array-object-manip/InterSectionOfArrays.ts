// https://leetcode.com/problems/intersection-of-two-arrays/description/

// 349. Intersection of Two Arrays

// Given two integer arrays nums1 and nums2, 
// return an array of their intersection. 
// Each element in the result must be unique
//      and you may return the result in any order.


// PLAN
// This should be quite easy, unless I'm missing something
// make dupeTracker

// const solution = []

// for num in nums1:
// if num not in dupeTracker, dupeTracker[num] = 1
// If it is in dupetracker, do nothing

// for num in nums2:
// Now we know what nums are in nums1
// If dupeTracker[num] === 0, 
//      solution.push(num)
//      dupeTracker[num] ++
//      That way we know it's already been accounted for in solution

// I'm sure there's a more elegant way to do this but it should work

function intersection(nums1: number[], nums2: number[]): number[] {
    
    const dupeTracker: Record<number, number> = {}
    const solution: number[] = []

    for (const num of nums1){
        dupeTracker[num] = 0
    }

    for (const num of nums2){
        if (dupeTracker[num] === 0){
            solution.push(num)
            dupeTracker[num] +=1 // so we know it's already in solution
        }
    }

    return solution
};

// console.log(intersection([1,2,2,1], [2, 2])) // [2]
console.log(intersection([4,9,5], [9,4,9,8,4])) // [9, 4]