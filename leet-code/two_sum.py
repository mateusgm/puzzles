# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums, inds = zip(*sorted(zip(nums, range(0,len(nums)))))
        i = 0
        j = len(nums)-1
        
        for _ in inds:
            total = nums[i] + nums[j]
            if total == target:
                return [inds[i],inds[j]]
            elif total < target:
                i += 1
            else:
                j -= 1        
        