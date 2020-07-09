# 输入：旋转数组，一个排序数组从中间某一位置截断，然后cat到后面。和一个检索的目标值target
# 输出：target在数组中的idx，若不在数组中返回-1

class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        i, j = 0, n-1
        while i <= j:
            mid = (i+j) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[i]:
                # mid左边有序
                if target <= nums[mid] and nums[i] <= target:
                    j = mid -1
                else:
                    i = mid+1
            else:
                # mid右边有序
                if target <= nums[j] and nums[mid] <= target:
                    i = mid +1
                else:
                    j = mid -1
        return -1

# 第一层划分：nums[mid] >= nums[i]那么左半边是有序的，否则右半边是有序的。其中判断式中的等号一定要有。
# 第二层划分：如果左半边有序，target在不在有序内部。如果右半边有序target在不在有序内部，调整左右边界。
