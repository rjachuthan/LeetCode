# EASY
# Given an array of integers 'num' and an integer 'target', return indices of
# of the two numbers such that they add up to 'target'.

# You must assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

# Example 1:
# INPUT - nums = [2, 7, 11, 15], target = 9
# OUTPUT - [0, 1]
# OUTPUT - Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# INPUT - nums = [3, 2, 4], target = 6
# OUTPUT - [1, 2]

# Example 3:
# INPUT - nums = [3, 3], target = 6
# OUTPUT - [0, 1]

# Constraints
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

# Follow-up: Can you come up with an algorithm which is less than O(n^2) time
# complexity?

from typing import List, Dict

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Runtime: 6540ms; Memory: 14.8 MB"""
        ans:List = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
        return ans
    
    def twoSumFaster(self, nums:List[int], target: int) -> List[int]:
        """Runtime: 128ms; Memory: 15.7 MB"""
        ans:List = []
        mem:Dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] not in mem:
                mem[difference] = i
            else:
                ans = [mem[nums[i]], i]
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.twoSumFaster(nums=[2, 7, 11, 15], target=9))
    print(a.twoSumFaster(nums=[3, 2, 4], target=6))
    print(a.twoSumFaster(nums=[3, 3], target=6))
