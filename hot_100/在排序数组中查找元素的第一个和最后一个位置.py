# 在一个排序数组中，有重复的元素。给定一个目标值，如果数组中不存在这个目标值，那么就返回[-1, -1]，否则返回在数组中target的第一个位置和最后一个位置

# mycode
# 使用了二分法嵌套一个二分法，实际上只需要对数组分别进行两次二分遍历就可以了。不需要嵌套。
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        res = [-1, -1]
        while i<=j:
            mid = (i+j)//2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                res = [mid, mid]
                mid_r, mid_l = mid-1, mid+1
                while i <= mid_r:
                    mid = (i + mid_r)//2
                    if nums[mid] == target:
                        res[0] = mid
                        mid_r = mid - 1
                    elif nums[mid] > target:
                        mid_r = mid - 1
                    else:
                        i = mid + 1
                while mid_l <= j:
                    mid = (j + mid_l)//2
                    if nums[mid] == target:
                        res[1] = mid
                        mid_l = mid + 1
                    elif nums[mid] < target:
                        mid_l = mid + 1
                    else:
                        j = mid - 1
                return res
        return res

# improved
class Solution:
    def searchRange(self, nums, target: int):
        def helper(nums, left=True):
            n = len(nums)
            i, j = 0, n - 1
            res = -1
            while i <= j:
                mid = (i + j) // 2
                if left:
                    if nums[mid] >= target:
                        j = mid - 1
                        if nums[mid] == target:
                            res = mid

                    else:
                        i = mid + 1
                else:
                    if nums[mid] >= target:
                        j = mid - 1
                        if nums[mid] == target:
                            res = mid
                    else:
                        i = mid + 1
            return res
        
        idx_l = helper(nums, True)
        idx_r = helper(nums, False)
        return [idx_l, idx_r]
