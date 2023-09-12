# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, string):        
        c_index = defaultdict(int)
        l = 0
        longest = 0

        for r,c in enumerate(string):
            if c in c_index:
                l = max(l,c_index[c]+1)
            c_index[c] = r
            longest = max(longest, r-l+1)
                    
        return longest