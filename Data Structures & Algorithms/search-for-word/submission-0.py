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