# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        merged = []
        for (b,e) in sorted(intervals, key=lambda x: x[0]):
            if merged and b <= merged[-1][1]:
                merged[-1][1] = max(e,merged[-1][1])
            else:
                merged.append( [b,e] )
        return merged