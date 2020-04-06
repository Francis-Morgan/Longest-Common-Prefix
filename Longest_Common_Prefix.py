class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        function to find the longest common prefix string amongst an array of strings
        
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:                       # if input string is empty we output empty string
            return ""
        min_st = min(strs)                       # we assing the variable min_st to the first alphabetical word in out input list               
        max_st = max(strs)                       # the last word                                   
        
        for i in range(len(min_st)):             # the number of iterations == the length of the minimum word
            if max_st[i] != min_st[i]:           # check the words for similarity
                return max_st[:i]                # if the character no same - output longest common prefix 
        return min_st                            # if the words match exactly, return shorter of them
