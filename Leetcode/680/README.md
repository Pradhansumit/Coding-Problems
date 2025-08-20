# 680. Valid Palindrome II

## Problem -> 

**Easy**

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

## Output ->
Return true or false whether word is palindrome or not after deleting a character from it.

## Thought process ->
Using two pointers at the both ends use while loop to move towards center. First loop will just check if the both ends are same or not. When both ends moving toward each other does not seems equal then it will cause another loop to check if taking off one character from either left or right will make it palindrome or not. If it is then final answer will be palindrome otherwise it is not palindrome.