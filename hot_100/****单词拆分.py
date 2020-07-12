# 输入：字符串，候选单词列表
# 输出：字符串是否可以拆分成单词列表中的元素

# mycode，使用了递归，超时了，代码太复杂
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if not s:
            return True
        if not wordDict:
            return False
            
        n = len(s)
        dp = [False for _ in range(n)]

        def helper(i, s):
            n = len(s)
            if not n:
                return
            j = 0
            while j < n:
                if s[:j+1] in wordDict:
                    dp[i+j] = True
                    helper(i+j+1, s[j+1:])
                j += 1
            return
        helper(0, s)
        return dp[-1]
# 考虑如果提前结束的话是不是可以控制在时间范围内？
# 不能！！！！！！！


# 官方答案
# 使用dp保存的是，dp[i]包含i在内的字符串的前i个元素时候可以拆分。然后检索接下来的到字符串截止的内容是否是一个单词
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False
        
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                if dp[-1]:
                    return True
        return False
