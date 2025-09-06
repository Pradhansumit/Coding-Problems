# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

**EASY**

### Problem Description:
You are climbing a staircase. It takes **n** steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:**
Input: n = 2
Ouput: 2
Explaination: There are two ways to climb to the top.
1. 1 Step + 1 Step
2. 2 Steps

**Examples 2:**
Input: n = 3
Ouput: n = 3
Explaination: There are three ways to climb to the top.
1. 1 Step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

### Thought Process
We can use the concept of memoization. In this way we would keep the result of every recursion in dictionary. This would reduce the computation timing and would prevent from TLE.