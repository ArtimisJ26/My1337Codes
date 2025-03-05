class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)

        for i in range(n):
            num = nums[i]

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            
            if freq[num] > (n/2):
                return num