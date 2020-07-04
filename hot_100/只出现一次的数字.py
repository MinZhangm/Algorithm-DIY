# list中只有一个数字只出现了一次，其余都是出现了两次
# 输出，这个只出现了一次的数字

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[0] ^= nums[i]
        return nums[0]
# ^:异或运算
# 0和任何数字异或都是数字本身
