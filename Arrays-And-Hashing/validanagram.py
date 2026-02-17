# Valid Anagram
# Easy
# Hints
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true
# Example 2:
# Input: s = "jar", t = "jam"
# Output: false
# Constraints:
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
# Time Complexity: O(n log n) where n is the length of the input strings. This is because sorting the strings takes O(n log n) time.
# Space Complexity: O(n) in the worst case, if all characters in the input strings are unique, the sorted strings will contain all n characters.