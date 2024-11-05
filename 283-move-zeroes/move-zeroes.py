class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums

        l = 0
        r = 1
        
        while r < n:
            if nums[l] == 0:
                while nums[r] == 0:
                    r += 1
                    if r > n-1:
                        return nums
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
            l += 1
            r += 1
        return nums