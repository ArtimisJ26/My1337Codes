class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefixes = [1] * len(nums) 
        sufixes = [1] * len(nums) 
        res = [1] * len(nums) 

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            sufixes[j] = sufixes[j+1] * nums[j+1]
        
        for k in range(len(nums)):
            res[k] = prefixes[k] * sufixes[k]
        
        return res