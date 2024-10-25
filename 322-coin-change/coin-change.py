class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def exploreCombinations(balance):
            if balance == 0:
                return 0
            
            if balance < 0:
                return -1
            minCoins = float('inf')
            for coin in coins:
                res = exploreCombinations(balance - coin)
                if res != -1:
                    minCoins = min(minCoins, res + 1)
            return minCoins if minCoins != float('inf') else -1
                
        return exploreCombinations(amount)




# class Solution:
#     # Bottom-Up (Tabulation)
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         # Base case; zero coins needed for amount zero.
#         dp[0] = 0  

#         # Fill the dp array for each coin.
#         for coin in coins:
#             for amt in range(coin, amount + 1):
#                 # Update the minimum coins needed for the current amount.
#                 dp[amt] = min(dp[amt], dp[amt - coin] + 1)

#         # Return the result for the target amount.
#         return dp[amount] if dp[amount] != float('inf') else -1