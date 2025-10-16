# [2598. Smallest Missing Non-negative Integer After Operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/)

**MEDIUM**

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 

Constraints:

1 <= nums.length, value <= 105
-109 <= nums[i] <= 109

### THOUGHT PROCESS

When you first read the problem, the key is to focus on what the allowed operation — adding or subtracting `value` any number of times — really means. If you think about it, adding or subtracting `value` repeatedly doesn’t change a number’s remainder when divided by `value`. For example, if `value = 5`, then 7, 12, and -3 all have the same remainder 2 modulo 5. This realization simplifies the problem dramatically, because it means that each element in the array can only ever represent numbers that share its remainder with respect to `value`. So, instead of thinking about all the infinite numbers we could make, we only need to care about the **remainders** and how many times each remainder appears in the array.

Once you understand that, the problem becomes one of distributing these remainder “tokens.” Each element gives you one token for its remainder. Then, imagine you start counting integers from 0 upward. The integer 0 requires remainder 0, 1 requires remainder 1, and so on. Every time you can form a number, you “spend” one token from that remainder’s pile. Eventually, one of the remainder piles runs out — meaning you no longer have a number in the array that can produce another value with that remainder. That’s the point where you get stuck, and the current integer is the smallest non-negative number you cannot form.

So the deep insight is recognizing that this is not about performing infinite operations or simulating additions and subtractions directly. It’s about realizing the invariant — that remainders stay constant — and converting the problem into a simple counting process over remainder groups. Once that clicks, the rest of the problem becomes straightforward to reason about.
