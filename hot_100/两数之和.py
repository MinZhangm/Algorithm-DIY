输入： nums（备选列表）, target(两数之和)
输出：返回和为target的两数的index

# mycode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            tgt = target - nums[i]
            j = i + 1
            while j < n:
                if tgt == nums[j]:
                    return [i, j]
                j += 1
            i += 1
        return None

# amz
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            tgt = target - nums[i]
            if tgt in hash_map.keys():
                return [i, hash_map[tgt]]
            hash_map[nums[i]] = i
        return None
