class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buy or selling
        # if buy > i + 1
        # if sell > i + 2

        dp = {} # key = (i, buying) val = max_profit

        def dfs(i, buying):
            # base case i = out of bounds
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying: 
                buy = dfs(i +1, False) - prices[i] # Buy today
                cooldown = dfs(i+1, True)  # skip today

                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = dfs(i+2, True) + prices[i] # sell today
                cooldown = dfs(i+1, buying) # sell  next day

                dp[(i,buying)] = max(sell,cooldown)

            return dp[(i, buying)]

        return dfs(0, True)

        