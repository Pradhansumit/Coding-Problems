# [1304. Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

## Problem -> 

**EASY**
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000

## Output ->
Return an array of integers that contains the number of positive and negative digits which sums up to 0. Also if the given number is odd, add a 0.

## Thought process ->
First check if the number is odd or even. Odd would require an extra number and that is 0. Otherwise we would add positive and negative side of same number that would sum up to zero. Loop and add the numbers till the length is equal to the given number.