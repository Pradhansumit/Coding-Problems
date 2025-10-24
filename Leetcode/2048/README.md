[2048. Next Greater Numerically Balanced Number](https://leetcode.com/problems/next-greater-numerically-balanced-number/)

**MEDIUM**

An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106

### THOUGHT PROCESS
For going via Brute Force we only need to check if the count of digits in the number is same as the number value. For example in `3133` we can see that the count of 1 is 1 and count of 3 is 3, which means count is equal the value of the number. All we need to do now is that we use hashmap to count. If all the count is equal to values then we return the number otherwise we are going to increment the number by 1, and check the same for next number.