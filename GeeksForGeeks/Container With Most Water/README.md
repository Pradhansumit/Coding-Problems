#[Container With Most Water](https://www.geeksforgeeks.org/problems/container-with-most-water0535/1)

**MEDIUM**

## Problem Description

Given an array arr[] of non-negative integers, where each element **arr[i]** represetns the height of the vertical lines, find the **maximum amount of water** that can be contained between any two lines, together with x-axis.

_**Note:** In the case of a single line it will not be able to hold water._

**Examples**

**Input:** arr[] = [1, 5, 4, 3]
**Output:** 6
**Explaination:** 5 and 3 are distance apart. So the size of the base is 2. Height of container = min(5,3) = 3. So, total area to hold water = 3 * 2 = 6.

**Input:** arr[] = [3, 1, 2, 4, 5]
**Output:** 12
**Explaination:** 5 and 3 are 4 distance apart. So the size of the base is 4. Height of conatiner = min(5, 3) = 3. So, total area to hodl water = 4 * 3 = 12.

**Input:** arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
**Output:** 25
**Explaination:** 8 and 5 are 5 distance apart. So the size of the base is 5. Height of container = min(8,5) = 5. So, the total area to hold water = 5 * 5 = 25.

Constraints:
1 ≤ arr.size() ≤ 10^5
0 ≤ arr[i] ≤ 10^4

### Thought Process
While the problem seem obvious enough for using two pointers. We take the two pointers towards center from the ends of the array. Why? Because we want maximum base/distance between the heights, giving us max area. We would increase left pointer by 1 if value at left index is lower that right pointer and reduce right pointer by 1 if the value at right index is lower than left pointer. Otherwise, we need both to shift by 1.