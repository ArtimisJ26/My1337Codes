class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        
        return prefix.count(0)