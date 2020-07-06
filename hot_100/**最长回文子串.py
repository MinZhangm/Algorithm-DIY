# 输入：字符串
# 输出：最长回文子串内容

# 处理回文的基本思路：
#   1. 如果一个字符串是回文串，那么首尾一定是相等并且掐头去尾后也还是回文串
#   2. 反转之后与翻转之前相等

# 动态规划：d[i][j] = dp[l+1][t-1] and s[l] == s[r]
# 外层循环位置也十分重要，需要从每一个开始位置的最短长度开始循环，所以外层循环是子串长度，内层循环是子字符串的起始位置

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        tmp = 0
        dp = [[None for _ in range(n)] for _ in range(n)]
        # 左边的开始边界，不行，需要先固定子串长度
        for i in range(n):
            # 右边的结束边界， 不行，这意味是左边起始位置
            for l in range(n):
                # 可以根据左边位置和子字符串长度，确定右边位置
                r = i + l
                if r >= n:
                    break

                if i == 0 or (r - l == 1 and s[l] == s[r]):
                    dp[l][r] = True
                elif s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                else:
                    dp[l][r] = False

                if dp[l][r] and tmp < (r - l + 1):
                    tmp = r - l + 1
                    res = s[l:r + 1]
        return res
