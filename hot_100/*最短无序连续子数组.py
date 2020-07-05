# 输入：list
# 输出：最短无序子数组的长度，只需要对这部分子数组进行排序就可以获得一个升序数组

# 排序，比较，返回不同的部分长度
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1

# 双指针
# 只要最小值和最大值不在当前观察的数组范围的头和尾就得开始计入无序长度
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            Max = max(nums[l:r+1])
            Min = min(nums[l:r+1])
            if nums[l] == Min:
                l += 1
            elif nums[r] == Max:
                r -= 1
            else:
                break
        return len(nums[l:r+1])
        
# 两次遍历，一次找右边界和最大值，一次找左边界和最小值。
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        max_num=nums[0]
        right=0
        for i in range(n):
            if(nums[i]>=max_num):
                max_num=nums[i]
            else:
                right=i
        left=n
        min_num=nums[-1]
        for i in range(n-1,-1,-1):
            if(nums[i]<=min_num):
                min_num=nums[i]
            else:
                left=i
        return right-left+1 if(right-left+1 >0) else 0
