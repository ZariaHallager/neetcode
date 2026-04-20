# Word Search
# Medium
# Topics
# Company Tags
# Hints
# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:



# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"

# Output: true
# Example 2:



# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"

# Output: false
# Constraints:

# 1 <= board.length, board[i].length <= 5
# 1 <= word.length <= 10
# board and word consists of only lowercase and uppercase English letters.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[k]:
                return False

            visited[i][j] = True
            res = (backtrack(i + 1, j, k + 1) or
                   backtrack(i - 1, j, k + 1) or
                   backtrack(i, j + 1, k + 1) or
                   backtrack(i, j - 1, k + 1))
            visited[i][j] = False
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False