# 输入，已经中了一部分，list，1表示该位置中了花，0表示没种。n待种的花的数目。
# 输出，能否把n都种进去。
# 相邻不能种
# 同打家劫舍

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [1, 0] + flowerbed + [0, 1]
        total = len(flowerbed)
        i = 0
        patch = []

        while i < total and n >= 0:
            tmp = 0
            l = i
            while l < total and flowerbed[l] == 0:
                l += 1
            if l != i:
                if int((l-i-1)/2):
                    n -= int((l-i-1)/2)
                    if n <= 0:
                        return True
            i = l + 1
        return n <= 0
