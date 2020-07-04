# 输入：列表
# 输出：列表中出现次数超过n/2的元素。

# mycode，先快排，找到中间的元素，超时了。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        def qsort(a):
            n = len(a)
            if n <= 1:
                return a
            l = []
            r = []
            for i in range(1, n):
                if a[i] < a[0]:
                    l.append(a[i])
                else:
                    r.append(a[i]) 
            tmp = qsort(l) + [a[0]] + qsort(r)
            return tmp
        sorted_nums = qsort(nums)
        return sorted_nums[(n)//2]

# 投票法
# 维护候选众数，和众数的计数count， 最终的cand就是众数，因为如果是众数count+1，不是众数count-1，最终结果一定大于零。因为众数个数大于n/2。
# 如果count为零，那么就将下一个list中的元素作为新的众数的可能候选。
# 为啥是下一个？count为零时，不一定非得是下一个idx作为下一个cand的候选。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        count = 1
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] == cand:
                count += 1
            else: count -= 1
            if count == 0:
                cand = nums[i]
                count += 1 
            i += 1
        return cand

# 递归，秋梅一段的众数
# 如果n == 1的list，就直接是众数，如果左右的众数相同，那么就是这个众数，果果左右众数不同，通过比较左右众数出现的次数来确定整个list的众数
class Solution:
    def majorityElement(self, nums) -> int:
        n = len(nums)

        def helper(l, r):
            sub_n = len(nums[l:r])
            if sub_n <= 1:
                return nums[l]
            else:
                mid = (l + r) // 2
                mm_l = helper(l, mid)
                mm_r = helper(mid, r)
                if mm_l == mm_r:
                    return mm_l
                else:
                    count_l = sum(1 for x in nums[l:mid] if x == mm_l)
                    count_r = sum(1 for x in nums[mid:r] if x == mm_r)
                    if count_r > count_l:
                        return mm_r
                    else:
                        return mm_l
        return helper(0, n)
