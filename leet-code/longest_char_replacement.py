# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict

class Solution(object):

    def characterReplacement(self, s, k):
        max_len = 0
        c_max = l = 0
        c_freq = defaultdict(int)

        for r,c in enumerate(s):
            c_freq[c] += 1
            if c_freq[c] > c_freq[c_max]:
                c_max = c
            
            if r-l+1 > k + c_freq[c_max]:
                c_freq[ s[l] ] -= 1
                l += 1

            longest = min(c_freq[c_max] + k, r-l+1)
            max_len = max(max_len, longest)

        return max_len