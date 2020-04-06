# first
**Task:**
[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

We need write a function to find the longest common prefix string amongst an array of strings.

For example, an array is given: ['sunset','superstition','surname']. Our function must return it: 'su', because 'su' - longest common prefix of these words. 

**SOLUTION TASK**
---
#### Algorithm for solving
We use min () and max () for array strings. We get the first and last word in the array 
(off the index of course, but by the number of the first character in the ASCII).
If the first character in the last word and in the first word matches, we will check the next character.
It's obvious that if the first and last word are different, they don't have the first common symbol.
And if they match, all words in the list start with the same symbol.
#### Code explanation
Firstly, find the minimum and maximum element of our list:
   
    min_st = min(strs)                                    
    max_st = max(strs)

When we found the minimum and maximum (first or last character number in ASCII),
we will check the similiarity of these words:


    for i in range(len(min_st)):
        if max_st[i] != min_st[i]:
            return max_st[:i]
    return min_st

The number of iterations is equal to the length of the minimum word, because if our words match, we must output what is shorter.
If the maximum and minimum elements are the same then all the words in this list begin with the same letter and so on.
Else we output empty string.

**TEST PROGRAM**

In picture we can see runtime our program and memory usage.
![](https://github.com/chichikow/first/blob/master/test-picture.PNG)

**INPUT/OUTPUT**

![](https://github.com/chichikow/first/blob/master/test_picture.PNG)

