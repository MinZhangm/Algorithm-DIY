# 输入：list
# 输出：所有的不重复的，三个和为零的元素的list

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                second = nums[j]
                k = n-1
                while k > j and -nums[i] - nums[j] < nums[k]:
                    k -= 1
                if k == j:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
        return res
# 重难点在于如何简化计算
# 先排序，然后对于重复的元素，可以重复利用，但是不能作为重复的起始值。
# 对于最后一个元素，如果-nums[second] - nums[n-1] > nums[third]，那么就没有检索的必要了.或者遍历之后，指针重叠了，遍历到头都没有找到second==third，也返回。
