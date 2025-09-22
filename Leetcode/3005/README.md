# [3005. Count Elements With Maximum Frequency](https://leetcode.com/problems/count-elements-with-maximum-frequency/)

**EASY** 

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

### THOUGHT PROCESS

PROCESS 1: 
STEP 1: CALCULATE the count of occurence of each element using HASH TABLE.
STEP 2: Sort them with values in descending order.
STEP 3: Loop through the values and search for other maximum values and count the values.
STEP 4: Return the counted values.

PROCESS 2:
STEP 1: CALCULATE the count of occurence of each element using HASH TABLE.
STEP 2: Find the max value in the HASH TABLE using MAX Function().
STEP 3: Loop and check if there are any other element in nums (using set to reduce the iteration) with same value as the MAX Value.
STEP 4: Count the occurence of the max occurence values.
STEP 5: Return the counted values.