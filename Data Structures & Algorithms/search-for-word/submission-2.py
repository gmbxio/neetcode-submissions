class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(idx, row, col):
            if idx == len(word):
                return True

            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or
                (row, col) in path or 
                word[idx] != board[row][col]):
                return False
            
            path.add((row, col))
            res =   (dfs(idx + 1, row + 1, col) or
                    dfs(idx + 1, row, col + 1) or
                    dfs(idx + 1, row - 1, col) or
                    dfs(idx + 1, row, col - 1))
            path.remove((row, col))
            return res
        
        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True 
        return False 
