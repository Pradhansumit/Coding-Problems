# 424. Longest Repeating Character Replacement

## Problem -> 

**MEDIUM**

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

## Output ->
Return the length of the longest substring having the same letter after changing k different letters. 

## Thought process ->
It is a problem of sliding window. We need to keep track/counts of letters in the window. Also need to check the maximum same letters. We can do this by subtracting the size of current window length and the maximum occuring letter. If the subtraction is greater than k given then we need to reduce the size of the window from left also need to subtract the letter count.