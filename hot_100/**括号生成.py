# 输入，需要生成多少组括号
# 输出：所有合法的情况

class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def helper(s, count_l, count_r):
            if count_l > n or count_l > n:
                return
            if count_l == count_r and count_l == n:
                res.append(s)
                return
            if count_l == count_r:
                helper(s + '(', count_l + 1, count_r)
            else:
                if count_l < n:
                    helper(s + '(', count_l + 1, count_r)
                helper(s + ')', count_l, count_r+1)

        helper('', 0, 0)
        return res
