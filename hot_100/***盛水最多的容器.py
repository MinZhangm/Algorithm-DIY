# 输入：表示每根目标的高度的列表
# 输出：能够装入的最多的水的面积

# 暴力超时，双指针
# 两个指针，头、尾，每次移动指向较短的高度的指针
# min(i, j) * dis，如果移动指向较高的高度的指针，一定不会使结果变大。dis在减小，两个指针相向移动，高度由最短的高度决定，所以一定不会变大

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        tmp = 0
        while i < j:
            tmp = max(tmp, min(height[i], height[j]) *(j-i))
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return tmp
