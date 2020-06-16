#  双指针
class Solution:
    def removeDuplicates(self, nums):
        pre = 1
        while pre < len(nums):
            if nums[pre - 1] == nums[pre]:
                nums.pop(pre)
            else:
                pre = pre + 1
        return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
print(s.removeDuplicates(nums))
