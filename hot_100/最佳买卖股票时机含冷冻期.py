class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices:
            return 0

        dp = [[None for _ in range(n)] for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]

        for i in range(1, n):
            # 0表示当前没有持有股票，前一天卖出了，今天卖出了
            dp[0][i] = max(dp[0][i-1], dp[1][i-1]+prices[i])
            # 1表示当前持有股票，前一天没有（不是刚刚卖出）今天刚买入，前一天就有今天还没卖出
            if i -2<0:
                dp[1][i] = max(dp[1][i-1], -prices[i])
            else:
                dp[1][i] = max(dp[1][i-1], dp[0][i-2]-prices[i])
        print(dp)

        return dp[0][-1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0 for _ in range(3)]for _ in range(n)]
        dp[0] = [-prices[0], 0, 0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0]+prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[-1])
