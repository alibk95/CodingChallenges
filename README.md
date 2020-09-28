# CodingChallenges
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

