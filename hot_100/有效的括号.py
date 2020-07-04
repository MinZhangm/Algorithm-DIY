# mycode
class Solution:
    def isValid(self, s: str) -> bool:
        re_dict = {'}':'{', ')':'(', ']':'['}
        n = len(s)
        i = 0
        stack = []
        while i < n:
            if s[i] in re_dict.values():
                stack.append(s[i])
                i += 1
            else:
                if not stack:
                    return False
                if re_dict[s[i]] == stack.pop():
                    i += 1
                else:
                    return False

        return True if not stack else False
# 提前判断字符串是偶数
# 直接返回时候是空栈
