# A. Tram

## Problem -> 
A tram runs on one line.
At ith stop a(i) passengers exit the tram,
while b(i) passengers enter it.

Note: Tram arrives with 0 passenger at the first stop.
And all the passengers leave the tram at the last stop.


## Output ->
Calculate the max capacity of the tram.

## Thought process ->
There will be a "count" variable that counts the max number of people
at any given stop. 
Max can be find out by checking number of passengers exiting the tram while
number of people entering the tram.

For e.g. at a given stop 
present stop: 3 passengers inside the tram
next stop: 2 passengers exit and 5 enters
so present passenger count: 3-2 + 5 = 6 
we need to track this count. 
The max count is the answer.

# Complexity
Time Complexity: O(n)
Space Complexity: O(1)