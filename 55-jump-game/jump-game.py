class Solution:
    def canJump(self, nums: List[int]) -> bool:   
        dp = [False] * len(nums)
        end = len(nums) - 1
        i = end
                
        while i >= 0:
            if i == end:
                dp[i] = True
            elif i + nums[i] >= end:
                dp[i] = True
            else:
                for jump in range(1, nums[i]+1):
                    if dp[i+jump]:
                        dp[i] = True
            i -= 1
        print(dp)
        return dp[0]