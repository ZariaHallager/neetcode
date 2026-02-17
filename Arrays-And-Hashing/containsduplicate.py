# Contains Duplicate
# Easy
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
    
# Time Complexity: O(n) where n is the length of the input array nums. This is because we need to iterate through the array to create a set of unique elements.
# Space Complexity: O(n) in the worst case, if all elements in the input array are unique, the set will contain all n elements. In the best case, if all elements are