class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        dp = {}
        res = max(1, counts[1] - 1 + counts[1]%2)
        arr = sorted([k for k,v in counts.items() if v >= 2 and k > 1], reverse=True)

        for num in arr:
            if num*num in dp:
                dp[num] = dp[num*num] + 2
                res = max(res, dp[num])
            elif num*num in counts:
                dp[num] = 3
                res = max(res, dp[num])
        return res