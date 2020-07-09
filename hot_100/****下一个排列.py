# 输入：一组数值
# 输出：这组数值的下一个字典序，如果已经是字典序的最后一个，就直接给出字典序的第一个

# 补充：字典序
# 字母：就是按照每一位字母的顺序排序
# 数字：就是按照每一位的数字大小排序，如果这一位相同，那么就比较下一位
# 字典序算法
# 我实在是理解不了，就死记硬背下来算了

# 从字符串的倒数第二位向idx=0遍历，如果出现nums[idx] < nums[idx+1]，记当前位置为a
# 再从自字符串最后一位开始向idx=0遍历，如果出现第一个大于nums[a]的值，记当前位置为b
# 交换ab对应的元素，ab仍然是原位置的指针
# 然后重新从小到大排序a后面的元素。
# 得到的就是下一个字典序。
# 特殊情况是：找不到a，那么就是倒序，也就是字典序的最后一个排序，直接返回正序的字符串即可。

# list的翻转可以直接，list_name.reverse()，无返回值，直接在原位置对list进行修改。

class Solution(object):
  def nextPermutation(self, nums) -> None:
          """
          Do not return anything, modify nums in-place instead.
          """
          n = len(nums)
          i = n-2
          while i >=0:
              if nums[i] < nums[i+1]:
                  break
              i -= 1
          if i < 0:
              nums.reverse()              # 尤其注意这里，使用nums = nums[::-1]就不行，但是nums[::] = nums[::-1]就行
          else:
              j = n - 1
              while j >= 0:
                  if nums[j] > nums[i]:
                      break
                  j -= 1
              nums[i], nums[j] = nums[j], nums[i]
              nums[i+1:] = sorted(nums[i+1:])
