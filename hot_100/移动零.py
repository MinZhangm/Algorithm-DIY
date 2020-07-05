# 把所有的非零元素移动到零元素前面，并且保持非零元素的位置
# 原位置修改，无返回

# 方法一：j永远指向零元素，如果遇到非零元素i，j一起移动，如果遇到零元素只有i移动

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] , nums[i]= nums[i] , nums[j]
                j += 1

# 方法二，大同小异，用count计0位置
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置
        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i - count], nums[i] = nums[i], 0
        return nums

# 小张的二傻子做法

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        # i记录最靠前的0的位置
        # j记录从i开始第一个非0的位置
        while j < n:
            while i < n-1 and nums[i] != 0:
                i += 1
            j = i + 1
            while j < n and nums[j] == 0:
                j += 1
            if j > n-1:
                break
            nums[i], nums[j] = nums[j], nums[i]

            i += 1
