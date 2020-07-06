# 裸写
class Solution():
    def bubble(self, nums):
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
        return nums

    def select(self, nums):
        n = len(nums)
        for i in range(n):
            min_tmp = nums[i]
            index_tmp = i
            for j in range(i, n):
                if nums[j] < min_tmp:
                    index_tmp = j
                    min_tmp = nums[j]
            nums[index_tmp], nums[i] = nums[i], nums[index_tmp]
        return nums

    def insert_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            j = i
            while j >= 1 and nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums

    def merge(self, nums):
        def helper(left, right):
            i, j, res = 0, 0, []
            if not left and not right:
                return []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                elif left[i] > right[j]:
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    res.append(right[j])
                    i += 1
                    j += 1
            if j < len(right):
                res.extend(right[j:])
            if i < len(left):
                res.extend(left[i:])
            return res

        n = len(nums)
        if n <= 1:
            return nums
        # mid = (n-1 + 0) // 2
        # left = self.merge(nums[:mid+1])
        # right = self.merge(nums[mid+1:])
        mid = n // 2                                # mid = (n-1+0) // 2出现一直循环返回[]的情况，永远取不到nums中的元素
        left = self.merge(nums[:mid])               #
        right = self.merge(nums[mid:])
        res = helper(left, right)
        return res

    def quict(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        tmp = nums[0]
        left = []
        right = []
        for i in range(1, n):
            if nums[i] > tmp:
                right.append(nums[i])
            else:
                left.append(nums[i])
        left = self.quict(left)
        right = self.quict(right)
        return left + [nums[0]] + right

    def heap(self, nums):
        def helper(nums, l, r):
            if not nums:
                return []
            # 注意，并不是左右孩子都存在
            while l < r and l *2 + 2 < r or 2*l + 1 < r:
                if 2*l + 2 < r:
                    if nums[2*l + 1] < nums[2*l + 2]:
                        nums[2*l + 1], nums[2*l + 2] = nums[2*l + 2], nums[2*l + 1]
                if nums[2*l + 1] > nums[l]:
                    nums[l], nums[2*l+1] = nums[2*l+1], nums[l]
                l += 1

        n = len(nums)
        if n <= 1:
            return nums
        # 从最后一个非叶子节点开始调整，维持节点比左右孩子大，这时不确定左右孩子那个更大
        # 但是调整之后，根节点是最大的
        # 最后一个非叶子节点的位置：n//2-1
        for i in range(n//2-1, -1, -1):
            helper(nums, i, n)
        for i in range(n-1, -1, -1):
            tmp = nums[i]
            nums[i] = nums[0]
            nums[0] = tmp
            helper(nums, 0, i)
        return nums
