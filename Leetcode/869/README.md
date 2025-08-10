# 869. Reordered Power of 2

## Problem -> 

**Medium**

You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.
 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:
1 <= n <= 109

## Output ->
Basically return True if n is a power of 2 after rearranging the digits. Otherwise, return False.

## Thought process ->
Turn n (variable provided) to string and then sort it.
Loop from 0 to 31 and calculate power of 2.
Convert this power value to string and sort it too.
Check if the n (string and sorted) is same as power value (string and sorted).
If equal return True otherwise False.