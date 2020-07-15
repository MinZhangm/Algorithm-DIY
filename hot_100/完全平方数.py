# 输入一个数字，返回和为这个数字的最少的完全平方数的个数

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf') for _ in range(n+1)]
        square = [i**2 for i in range(int(math.sqrt(n))+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for j in square:
                if i - j < 0:
                    break
                dp[i] = min(dp[i], dp[i-j]+1)                    
        return dp[-1]
