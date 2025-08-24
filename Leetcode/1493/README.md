# 1493. Longest Subarray of 1's After Deleting One Element

## Problem -> 

**MEDIUM**

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

## Output ->
Return the max window size after deleting atmost one 0 number.

## Thought process ->
Take two pointers left and right. Right is for moving forward and left is for managing the size of windows. If the count of 0s is more than 1 then it is needed to move left forward till the count of 0s is 1.