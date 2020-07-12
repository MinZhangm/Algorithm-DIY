# 输入：list
# 输出：乘积最大的子数组的乘积，子数组要求是连续的。

# 二维的dp超时，一维的dp就可以满足条件
# 需要同事维护一个最大的数组和一个最小的数组，因为有负数的存在
# dp表示的是以当前的节点作为子数组的最后一个节点（或者第一个也是最后一个结点的时候，最大的乘积）
# 单独维护一个结果变量，不停的与dp中求得的当前的结果进行比较。


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp_max = [None for _ in range(n)]
        dp_min = [None for _ in range(n)]
        dp_min[0] = nums[0]
        dp_max[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            res = max(res, dp_max[i])
        return res
