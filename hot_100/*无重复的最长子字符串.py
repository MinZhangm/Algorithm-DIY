# 输入字符串
# 输出最长的无重复的连续子字符串的长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        res = 0
        hash_dict= set()
        for i in range(n):
            while j < n and s[j] not in hash_dict:
                hash_dict.add(s[j])
                j += 1
            res = max(res, len(hash_dict))
            hash_dict.remove(s[i])
        return res
 # 维护两个指针，left当前判断的子串的起点，right为当前判断的子串的终点，并且这个点在每次i刚刚结束上一次循环的时候不发生变化。
