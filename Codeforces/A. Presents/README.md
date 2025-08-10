# A. Magnets

__link:[A. Presents](https://codeforces.com/problemset/problem/136/)__ 

## Problem -> 
Petya invited n friends, numbered from 1 to n.

Each friend gave a gift to exactly one other friend (could even be themselves).

You are given a list describing who each friend gave a gift to.

You must figure out the reverse mapping:

For each friend from 1 to n, figure out who gave them a gift.

## Output ->
Print n space-separated integers: the i-th number should equal the number of the friend who gave a gift to friend number i.

## Thought process ->
We have to find out the position of the numbers (1-indexed) from the second line.

Example
4 <- Number of friends
2 3 4 1 

Friend 1 gave a gift to Friend 2
Friend 2 gave a gift to Friend 3
Friend 3 gave a gift to Friend 4
Friend 4 gave a gift to Friend 1 

Res -> 4 1 2 3
simply find the 1-based index of the numbers 
1 -> 4
2 -> 1
3 -> 2
4 -> 3


