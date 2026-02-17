# Group Anagrams
# Medium
# Hints
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
# Example 3:
# Input: strs = [""]
# Output: [[""]]
# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
# Time complexity: O(n * k log k), where n is the number of strings in the input array and k is the maximum length of a string. Sorting each string takes O(k log k) time, and we do this for all n strings.
# Space complexity: O(n * k), where n is the number of strings in the input array and k is the maximum length of a string. In the worst case, all strings are anagrams of each other, and we store all n strings in the hash map, which takes O(n * k) space.   