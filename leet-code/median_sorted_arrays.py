# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = 0
        last = blast = None
        n = len(nums1)+len(nums2)
        mid = int(n/2)
        cnt = 0
        while cnt <= mid:
            cnt += 1
            blast = last
            if i != len(nums1) and (j == len(nums2) or nums1[i] < nums2[j]):
                last = nums1[i]
                i   += 1
            else:
                last = nums2[j]
                j += 1
            print(i,j, last, blast)

        if mid*2 == n:
            return (last+blast)/2.0
        return last
