from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
