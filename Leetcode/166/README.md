# [166. Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/)

**MEDIUM**

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0


### THOUGHT PROCESS
First of all check if the numerator is 0. If it is then entire result is going to be 0. Then we need to check for the signs. So the result will be in negative if either of the numerator or denominator is negative. The process now for checking repeating numbers is done through long division process. We are going to have a dictonary mapping the numbers. We are going to divide remainder with the denominator repeatedly. If we see remainder in our map then we are going insert bracket at that index and then close the bracket at the end. Then break the loop. 

WHAT IS THE PATTERN IN THIS? 
-> TRACK REMAINDER => REPEATING REMAINDER MEANS REPEATING DECIMALS.