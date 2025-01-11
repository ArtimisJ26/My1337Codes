class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort_nums = list(sorted(set(nums)))
        res = 0
        i = 1
        consecutive = 1

        while i < len(sort_nums):
            if sort_nums[i] == sort_nums[i-1] + 1:
                consecutive += 1
            else:
                res = max(res, consecutive)
                consecutive = 1
            i += 1
        res = max(res, consecutive)
        return res