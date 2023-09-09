# https://leetcode.com/problems/top-k-frequent-elements/
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        
        return zip(*sorted(cnt.items(), key=lambda x: -x[1])[:k])[0]
