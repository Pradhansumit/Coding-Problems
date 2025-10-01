# [1518. Water Bottles](https://leetcode.com/problems/water-bottles/)

**EASY**

There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

 

Example 1:
![alt text](sample_1_1875.png)

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.


Example 2:
![alt text](sample_2_1875.png)

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
 

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100

### THOUGHT PROCESS
It is a simple problem of mathematics where we just have to count the filled bottles because that is what one is going to drink. We all need to keep count of the empty bottles because thats how we are going to exchange bottles, and getting filled ones.