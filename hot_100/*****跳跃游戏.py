# 输入：数组，每一位表示在当前位置上的最多的可向前移动的步数。
# 输出：是否能移动到最后一个位置上。

class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                break
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n-1:
                return True
        return False
# 只需要向前移动。维护一个可以到达的最远的idx。
# 遍历数组中的每一位
# 先判断当前的这个位置有没有超过最远的距离
# 如果没有那么更新最远距离
# 如果超过了直接返回False
