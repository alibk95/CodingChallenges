# CodingChallenges
**In order to test each function please take the related driver code out of the comments 
(Each function is indicated with a number which is also shows the related driver code).** 
## 1- moving zeros
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.<br>
Input: [0,1,0,3,12] <br>
Output: [1,3,12,0,0] <br>
Do this in-place without making a copy of the array.
Minimize the total number of operations.
<br>
## 2- Kth-largest 
Given a list, find the k-th largest element in the list. <br>
Input: list = [3, 5, 2, 4, 6, 8], k = 3 <br>
Output: 5 <br>
## 3- Single Number
Given a list of numbers, where every number shows up twice except for one number, find that one number. <br>
Challenge: Find a way to do this using O(1) memory. <br>
Input: [4, 3, 2, 4, 1, 3, 2] <br>
Output: 1
## 4- Two Sum
Given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k. <br>
Given [4, 7, 1 , -3, 2] and k = 5 <br>
return true since 4 + 1 = 5. <br>
Try to do it in a single pass of the list. <br>
2 solution is provided.
## 5- Longest length substring
Given a string, find the length of the longest substring without repeating characters. <br>
Input: "abcdefff" <br>
Output: 6 <br>
link to a useful video on how the algorithm works:
[link](https://youtu.be/WKTgajDkVcA)
## 6- Max Stack
class for a stack (called MaxStack) that supports all the regular functions (push, pop) and an additional function of max() which returns 
the maximum element in the stack (return None if the stack is empty). <br>
I tried to implement the max() function so that the time complexity is O(1). 
## 7- Balanced Parenthesis
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
Input: "((()))"
Output: True 
Input: "[()]{}"
Output: True 
Input: "({[)]"
Output: False 
## 8- Stock buy and sell
You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
## 9- Max contiguous subarray sum
You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array. <br>
Example: <br>
[34, -50, 42, 14, -5, 86]<br>
Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].<br>
Your solution should run in linear time ( O(n) ).
## 10- Simple Calculator 
Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. 
Assume the expression is properly formed. <br>
Input: - ( 3 + ( 2 - 1 ) ) <br>
Output: -4 
## 11- Course prerequisites
You are given a hash table where the key is a course code, and the value is a list of all the course codes that are
prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists,
return NULL. 
```
{
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
```
and the output should be as follows:<br>
```['CSC100', 'CSC200', 'CSCS300']```
## 12- Edit distance
Given two strings, determine the edit distance between them. The edit distance is defined as the minimum number of edits
(insertion, deletion, or substitution) needed to change one string to the other.<br>
For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t). <br>
the fist solution is done recursively with a time complexity of O(3^n). There are ways of doing it better like dynamic 
programming. 
## 13- Largest product
You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128. <br>
the first method is the simplest one which does it with 3 for loops and obviously not very efficient with the time
complexity of O(n^3) and space of O(1). <br>

the second method is more efficient when it does the following: <br>
1- Scan the array and compute Maximum, second maximum and third maximum element present in the array. <br>
2- Scan the array and compute Minimum and second minimum element present in the array. <br>
3- Return the maximum of product of Maximum, second maximum and third maximum and product of Minimum, second minimum and Maximum element. <br>
So all could be done in one single traversal of the array. So the time complexity comes down to O(n) with space of O(1).
## 14- Buddy string
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Example 1:
Input: A = "ab", B = "ba"
Output: true
## 15- Traverse a Grid
2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the 
bottom-right of the matrix y going only right or down. <br>
Example: <br>
n = 2, m = 2 <br>
This should return 2, since the only possible routes are: <br>
Right, down <br>
Down, right. <br>
This is done in a recursive method with an exponential time complexity which can be avoided by dynamic programming approach.
## 16- First and Last Indices of an Element in a Sorted Array
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a 
target element, x. Return -1 if the target is not found.

Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9 <br>
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150 <br>
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9 <br>
Output: [-1, -1]
## 17- Binary search tree 
Implement a simple binary search tree. <br>
This is done in a separate file called binary_tree.py. <br>
different functions are added to the BinaryTree class such as, insert(), find(), print() and so on. 
## 18- Look and say sequence
A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is 
obtained by describing the previous term. An example is easier to understand:
```
1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's. 
```
The task is, return the nth term of this sequence.
## 19- Number of Ways to Climb Stairs
You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 
steps at a time. Write a function that returns the number of unique ways to climb the stairs.
The simplest thing first comes to mind is to use recursive method.
## 20- Simple reverse of string
Reverse the string simply without using the builtin python "reverse" function. :  )
## 21- Falling Dominoes
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still <br>
L represents that the domino is falling to the left side <br>
R represents that the domino is falling to the right side <br>

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out
and that domino remains upright. <br>
Example: <br>
```
Input:  ..R...L..R.
Output: ..RR.LL..RR
```
## 22- Find Pythagorean Triplets
Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables
a, b, c where a2 + b2 = c2 <br>
Input: [3, 5, 12, 5, 13] <br>
Output: True <br>
## 23- FizzBuzz
We're given a number in the form of an integer n. <br>
Write a function that returns the string representation of all numbers from 1 to n based on the following rules: <br>
If it's a multiple of 3, represent it as "fizz".

If it's a multiple of 5, represent it as "buzz".

If it's a multiple of both 3 and 5, represent it as "fizzbuzz".

If it's neither, just return the number itself.

As such, fizzBuzz(15) would result in '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'.
## 24- Binary Search
Typical interview question.
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search 
target in nums. If target exists, then return True and its index, otherwise return False.
