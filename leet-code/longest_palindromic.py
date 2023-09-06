# https://leetcode.com/problems/longest-palindromic-substring/

from collections import defaultdict

class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        reverse_index = defaultdict(list) 
        
        for i,_char in enumerate(s):
            reverse_index[_char].append(i)
            
        
        biggest = s[0]
        for i,start in enumerate(s):
            for p in reverse_index[start]:
                if s[i:p+1] == s[i:p+1][::-1] and len(s[i:p+1]) > len(biggest):
                    biggest = s[i:p+1]
        
        return biggest