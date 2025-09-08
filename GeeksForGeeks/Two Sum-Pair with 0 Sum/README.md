# [Two sum -Pairs with 0 Sum](https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1)

**EASY**

Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

Examples:

Input: arr = [-1, 0, 1, 2, -1, -4]
Output: [[-1, 1]]
Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
arr[2] + arr[4] = 1 + (-1) = 0.
The distinct pair are [-1,1].
Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
Output: [[-6, 6],[-1, 1]]
Explanation: The distinct pairs are [-1, 1] and [-6, 6].
Expected Time Complexity: O(n log n)
Expected Auxiliary Space: O(n).

Constraints:
3 <= arr.size <= 10^5
-10^5 <= arr[i] <= 10^5

### Thought Process
We need to check if the negative / positive value is present in the set. If it is present than we need to return that. There can be multiple values. So it is best to use tuple and set. Set is for faster search. Preventing TLE errors.

