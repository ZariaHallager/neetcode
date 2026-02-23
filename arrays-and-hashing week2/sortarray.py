# Sort an Array
# Medium
# Topics
# Company Tags
# You are given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [10,9,1,1,1,2,3,1]

# Output: [1,1,1,1,2,3,9,10]
# Example 2:

# Input: nums = [5,10,2,1,3]

# Output: [1,2,3,5,10]
# Constraints:

# 1 <= nums.length <= 50,000.
# -50,000 <= nums[i] <= 50,000

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return self.sortArray(left) + middle + self.sortArray(right)