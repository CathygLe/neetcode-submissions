class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x] will store the MINIMUM number of coins needed to make amount x.
        # Start by assuming every amount is impossible -> infinity.
        dp = [float("inf")] * (amount + 1)

        # Base case: amount 0 needs 0 coins.
        dp[0] = 0 

        # Try to compute dp[1], dp[2], ..., dp[amount]
        for a in range(1, amount + 1):

            # Try every coin to see if we can use it to form amount 'a'
            for c in coins:

                # Only possible if coin value is not bigger than current amount.
                # Example: for amount 3, you cannot use coin 5.
                if a - c >= 0:

                    # dp[a-c] is: "How many coins to make the *remaining* amount?"
                    # +1 means: "If I use coin c now, that's one coin + whatever is optimal for a-c"
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    # This picks the BEST option among all coins

        # If dp[amount] is still infinity, no solution.
        return dp[amount] if dp[amount] != float("inf") else -1


        