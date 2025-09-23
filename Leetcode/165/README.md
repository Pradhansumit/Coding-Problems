# [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/description)

**MEDIUM**

Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.


### THOUGHT PROCESS

I can see the problem like comparing values left to right (also stated in question). It is in string so we need to make list (array) out of it. It can be done by splitting it with the "." (dots). We also need to make same length for version1 and version2. We can do that by filling 0s (as per the question). Then we can compare values left to right. We can take an extra step and map the values in integer so that when compared we don't have to convert the values into integers. That way we can save our time. After that as per the question if the version1 > version2 return 1 or version2 > version1 return -1 otherwise 0.

### ALGORITHM

The process is like subtracting decimals.

STEP 1: First step is we need to make an array of integers containing the integer version of all the values that we get after splitting the string with ".".
STEP 2: Then we are going to add extra zeros to array which has length less than the other just like doing in decimals.
STEP 3: We are going to loop each integers in version1 and version2.
STEP 4: As per question if version1 < version2 return -1. If version1 > version2 then return 1, otherwise return 0.
