# 输入：2-9分别表示不同的字母的一个列表，给定一个数字组成的字符串
# 输出：这些数字对应的所有字母按照顺序组合的所有情况

# mycode
# 三重循环
class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        n = len(s)
        code = {'2':['a', 'b', 'c'], 
        '3':['d','e','f'], 
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m','n', 'o'], 
        '7':['p', 'q','r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']}
        res = []
        for i in range(n):
            tmp = []
            if not res:
                tmp = code[s[i]]
                res = tmp
            else:
                for j in range(len(res)):
                    for idx in range(len(code[s[i]])):
                        tmp.append(res[j] + code[s[i]][idx]) 
                res = tmp
        return res

# 递归调用
# 时间复杂度：3^N*4^M
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []

        code =  {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def helper(l1, l2):
            if not l2 and l1:
                res.append(l1)
                return 

            for item in code[l2[0]]:
                helper(l1 + item, l2[1:])
        if not digits:
            return res       
        helper('', digits)
        return res
 # 注意这里 l1 +item并没有对l1进行修改，而是将相加之后的结果进行传递，保证了在返回之后，下一次的迭代递归l1的值不受影响
 # 如果是
 # l1 += item
 # 然后再： helper(l1, l2[1:])
 # 就需要在操作后，重新对修正一次l1已发生的变化了
 
