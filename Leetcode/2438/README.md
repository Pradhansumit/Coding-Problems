# 869. Range Product Queries of Powers

## Problem -> 

**Medium**
You are given a positive integer **n**. Create an array called **powers** which will store the numbers (power of 2) whose sum will be equal to n. Power (array) should be sorted.

You're also given a 2D integer array **queries**. 

queries[i] = [left(i), right(i)] -> Each queries[i] represent a query where you have to find the product of all powers[j] with left(i) <= j <= right(i).

Return an array answers, *equal in length to queries*.

Note: Since the answer to the ith query may be too large, each answers[i] should be returned modulo 10^9 + 7.


Example 1:

Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.
Example 2:

Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.
 

Constraints:

1 <= n <= 109
1 <= queries.length <= 105
0 <= start(i) <= end(i) < powers.length

## Output ->
Return the products of powers[i] from range queries[i][0] to queries[i][1].


## Thought process ->
First we need to work on building array called powers.
We have to select minimum numbers (power of 2) that sums to n.
But we can do it otherway using binary representation.
In binary representation we can take the power of 2 in powers array.
After the formation of powers array. All we have do is brute force multiplication of powers ranging from queries[i][0] to queries[i][1].
And append in the result array.
