from typing import List


class Solution:
    '''
    # Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4, 5, 6]
    target = 7
    print(s.twoSum(nums, target))
