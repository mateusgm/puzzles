# https://leetcode.com/problems/3sum/
class Solution(object):
    def search(self, nums, start, k):
        end = len(nums)
        while start != end:
            s = start+ (end-start)//2
            if nums[s] == k:
                return s
            if nums[s] > k:
                end = s
            elif nums[s] < k:
                start = s+1

    def threeSum(self, nums):
        nums = sorted(nums)
        i, j, k = 0,1,2
        triplets = set()
        while j < len(nums) and nums[i] <= 0:
            a,b = nums[i], nums[j]
            k = self.search(nums,j+1, -a-b)

            if k is not None:
                triplets.add((a,b,-a-b))

            j += 1
            if j == len(nums) or nums[i] + nums[j] > 0:
                i += 1 
                j = i+1
            
        return triplets
            
    def threeSumNaive(self, nums):
        ind, values = zip(*sorted(enumerate(nums), key=lambda x: x[1]))
        triplets = set()
        for i,a in enumerate(values):
            tot = a
            for j,b in enumerate(values):
                if ind[i] == ind[j]:
                    continue
                if a+b+values[0] > 0:
                    break
                for k,c in enumerate(values):
                    if ind[i] == ind[k] or ind[j] == ind[k]:
                        continue
                    if a+b+c > 0:
                        break
                    if a+b+c == 0:
                        triplets.add(tuple(sorted([a,b,c])))
        return list(triplets)
