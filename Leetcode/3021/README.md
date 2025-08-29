# 3021. Alice and Bob Playing Flower Game

## Problem -> 

**Medium**

Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.

![alt text](3021.png)

The game proceeds as follows:

Alice takes the first turn.
In each turn, a player must choose either one of the lane and pick one flower from that side.
At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

Alice must win the game according to the described rules.
The number of flowers x in the first lane must be in the range [1,n].
The number of flowers y in the second lane must be in the range [1,m].
Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

 

Example 1:

Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
Example 2:

Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.
 

Constraints:

1 <= n, m <= 105

## Output ->
Return the count of pairs that sum upto odd which means that Alice wins.

## Thought process ->
This problem is a question of **combinatorics** from discrete mathematics.
Alice picks the flower first and then Bob does. So the <u>*last flower needs to be picked by Alice*</u> to win this game. So we need to count the pairs from lane x and lane y that **sums up odd** (which mean last one to pick would be Alice, and Alice wins).
First, I thought of going using nested loops. But the range of n and m is too big causing TLE.
So it would be solved using **combinatorics**.
The formula is simple 
```Odd(n) * Even(n) + Odd(m) * Even(m)```.
