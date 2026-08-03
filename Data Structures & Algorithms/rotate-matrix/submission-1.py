class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(n):
            for c in range(0, r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        
