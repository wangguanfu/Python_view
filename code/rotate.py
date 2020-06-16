from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]

# 1. 暴力    2. 三次反转  3. 利用特性
