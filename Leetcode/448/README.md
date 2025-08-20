# 448. Find All Numbers Disappeared in an Array

## Problem -> 

**Easy**

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

## Thought process ->
Use a set instead of list because list causes a binary search which will be O(n). While doing this inside already running loop will cause it to run in O(n^2). Which is unnecessary. So it is better to use set. Set has O(1) for finding because it does lookup thing because it is behind the scene a hashing method.