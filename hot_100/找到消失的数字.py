# 输入：list，list中的左右元素都在[1, n]之间，有的出现了两次，有的只出现一次，找到没有出现的数字并返回
# 输出:list

# 不使用额外的空间
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
