# first
**Task:**
[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

We need write a function to find the longest common prefix string amongst an array of strings.

**SOLUTION TASK**
---
Firstly, find the minimum and maximum element of our list:
   
    min_st = min(strs)                                    
    max_st = max(strs)

When we found the minimum and maximum (first or last character number in ASCII),
we will check the similiarity of these words:


    for i in range(len(min_st)):
        if max_st[i] != min_st[i]:
            return max_st[:i]
    return min_st

If the maximum and minimum elements are the same then all the words in this list begin with the same letter and so on.
