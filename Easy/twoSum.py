"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given
Step 1 : nums = [2, 7, 11, 15], target = 9,
Step 2 : nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for pos, rec in enumerate(nums):
            otherNumber = target - rec
            try:
                if otherNumber in nums[:pos]:
                    return [pos, pos + 1 + nums[:pos].index(otherNumber)]
                elif otherNumber in nums[pos + 1:]:
                    return [pos, pos + 1 + nums[pos + 1:].index(otherNumber)]
            except ValueError:
                continue
        else:
            return None


if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
    print s.twoSum([3,4,2], 6)
    print s.twoSum([3,3], 6)