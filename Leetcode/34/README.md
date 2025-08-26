# 34. Find First and Last Position of Element in Sorted Array

## Problem -> 

**Medium**

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Output:
Return the first occurence and last occurence of the target value. IN O(LOG N). So do it using binary search.


## Thought process ->
Use a binary search to find the target and one greater then the target. One greater than target will give the index of the last occurence of the target + 1. Because they're sorted so when we does one less than we get the last occurence of the target.