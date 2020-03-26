class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_st = min(strs)                                    
        max_st = max(strs)                                      
        
        for i in range(len(max_st)):
            if max_st[i] != min_st[i]:
                return max_st[:i]
        return min_st
    
arr = Solution()
print(arr.longestCommonPrefix(['fly','flower','flame']))
