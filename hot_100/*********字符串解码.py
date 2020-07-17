class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        res = ''
        stack = []
        m = 0
        for i in range(n):
            if s[i] == '[':
                stack.append([m, res])
                m = 0                       # 记录当前字符串的重复次数
                res = ''                    # 记录当前这个[]内部的字符串内容
            elif s[i].isdigit():
                m = m*10 + int(s[i])        # 注意这里，数字不都指示一位的，两位及以上的数字，由于是一位一位的读入，所以需要十进制处理
            elif s[i] == ']':
                m_now, res_l = stack.pop()
                res = res_l + m_now * res
            else:
                res += s[i]
        return res
