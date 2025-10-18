// Another easy one
// I'm going to do this in one pass with two pointers

// https://leetcode.com/problems/valid-palindrome/description/

// A phrase is a palindrome if, 
// after converting all uppercase letters into lowercase letters,
// and removing all non-alphanumeric characters, 
// it reads the same forward and backward. 
// Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

// PLAN
// Two pointers
// Should be doable in one pass

// left = 0
// right = s.length -1

// Note that if left === right, that letter will be equal to itself obviously so we don't need to check it

// while left < right:
// {
// const leftChat, rightChar
// if lc isn't alphanumeric, left++
// if rc isn't alphanumeric, right--

// if lowercase lc === lowercase rc, 
//      left++ right--

// else return false
// }

// return true


function isPalindrome(s: string): boolean {
    
};