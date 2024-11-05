class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i):
            j = i
            while nums[j] == 0:
                j += 1
                if j > len(nums)-1:
                    return
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        for i, num in enumerate(nums):
            if num == 0:
                swap(i)

        return nums