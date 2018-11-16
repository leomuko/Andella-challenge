Mini-Max Sum
Given five positive integers, find the minimum and maximum values that can be calculated by summing
exactly four of the five integers. Then print the respective minimum and maximum values as a single line
of two space-separated long integers.
Input Format
A single line of five space-separated integers.
Constraints
Each integer is in the inclusive range .
Output Format
Print two space-separated long integers denoting the respective minimum and maximum values that can
be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit
integer.)
Sample Input
1 2 3 4 5
Sample Output
10 14
Explanation
Our initial numbers are , , , , and . We can calculate the following sums using four of the five
integers:
1. If we sum everything except , our sum is .
2. If we sum everything except , our sum is .
3. If we sum everything except , our sum is .
4. If we sum everything except , our sum is .
5. If we sum everything except , our sum is .
As you can see, the minimal sum is and the maximal sum is .
Thus, we print these minimal and maximal sums as two space-separated integers on a new line.
Hints: Beware of integer overflow! Use 64-bit Integer.