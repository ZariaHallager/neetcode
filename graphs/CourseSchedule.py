# Course Schedule
# Medium
# Topics
# Company Tags
# Hints
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[0,1]]

# Output: true
# Explanation: First take course 1 (no prerequisites) and then take course 0.

# Example 2:

# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

# Output: false
# Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= crs, pre < numCourses
# crs != pre
# All the pairs prerequisites are unique.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True