from typing import List


class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):  # [8]
            if nums[i] > 0: break  # [7]
            if i > 0 and nums[i] == nums[i - 1]: continue  # [1]

            l, r = i + 1, length - 1  # [2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:  # [3]
                    l += 1
                elif total > 0:  # [4]
                    r -= 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res


class Solution1:
    def threeSum(self, nums):
        """
        The recursive method actually skipped enough corner cases to get pass
        Leetcode's grader...

        Reduce to a 2-sum problem.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        if len(nums) < 3:
            return results

        self.recur_nSum(sorted(nums), 3, 0, [], results)
        return results

    def recur_nSum(self, nums, N, target, result, results):
        """
        N: this iteration solves an N-sum problem.
        target: the target sum of this iteration
        result: the current sub-result
        results: the results set
        """
        # early termination
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return

        if N == 2:
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s == target:
                    results.append(result + [nums[lo], nums[hi]])
                    lo += 1
                    # skip duplicates
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1

                elif s < target:
                    lo += 1
                    # skip duplicates
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                else:
                    hi -= 1
                    # skip duplicates
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
        else:
            # keep reducing
            for i in range(len(nums) - N + 1):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue  # skip duplicates
                # note how (target-nums[i]) here reduces unnecessary iterations
                self.recur_nSum(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]], results)
                

class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = 0
        c = len(nums) - 1
        output = []

        def recurse(a, c):
            if a < c:
                for b in range(a + 1, c):
                    sumOfNums = nums[a] + nums[b] + nums[c]
                    if sumOfNums == 0:
                        if sorted([nums[a], nums[b], nums[c]]) not in output:
                            output.append(sorted([nums[a], nums[b], nums[c]]))
                recurse(a + 1, c)
                recurse(a, c - 1)

        recurse(a, c)
        return output
