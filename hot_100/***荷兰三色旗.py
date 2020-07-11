# 输入数组，0,1,2分别表示不同的颜色；
# 输出按照数字大小进行排序的结果

# 官方答案，维护两个指针分别指向左边的第一个不为0的数和右边起第一个不为2的数
# 从左向右，到遇到2的指针结束
# 如果是0
# 遇到i指向0，那么就和0的指针交换，并且0的指针向前移位，i也向前移位
# 遇到i指向2，那么就和指向2的指针交换，并且2的指针向前移位，但是此时i不移位，因为不确定交换回来的是个什么数字
# 如果是1，那么直接i移位

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n -1
        # while r >= 0:
        #     if nums[r] != 2:
        #         break
        #     r -= 1
        # while l <n:
        #     if nums[l] != 0:
        #         break
        #     l += 1
        # i = l
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
                
# 我的，冒泡排序
