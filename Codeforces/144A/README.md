# [A. Arrival of the General](https://codeforces.com/problemset/problem/144/A)

**EASY**

Summary:
Problem Summary

There are n soldiers standing in a line with arbitrary heights.

According to the general, the line-up is correct if:

The first soldier is the tallest (maximum height).

The last soldier is the shortest (minimum height).

Heights of soldiers in between don’t matter.

In 1 second, the colonel can swap any two neighboring soldiers.

Task: Find the minimum number of seconds (swaps) needed to arrange the line so that the general considers it correct.


Examples
Input
4
33 44 11 22
Output
2
Input
7
10 10 58 31 63 40 76
Output
10
Note
In the first sample the colonel will need to swap the first and second soldier and then the third and fourth soldier. That will take 2 seconds. The resulting position of the soldiers is (44, 33, 22, 11).

In the second sample the colonel may swap the soldiers in the following sequence:

(10, 10, 58, 31, 63, 40, 76)
(10, 58, 10, 31, 63, 40, 76)
(10, 58, 10, 31, 63, 76, 40)
(10, 58, 10, 31, 76, 63, 40)
(10, 58, 31, 10, 76, 63, 40)
(10, 58, 31, 76, 10, 63, 40)
(10, 58, 31, 76, 63, 10, 40)
(10, 58, 76, 31, 63, 10, 40)
(10, 76, 58, 31, 63, 10, 40)
(76, 10, 58, 31, 63, 10, 40)
(76, 10, 58, 31, 63, 40, 10)

### Thought Process:
Find the index of the highest and the lowest number and move them to the first and the last respectively.