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