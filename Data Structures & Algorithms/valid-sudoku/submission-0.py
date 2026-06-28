class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                val = board[row][col]


                if val == ".":
                    continue

                rowKey = f"row_{row}_val{val}"
                colKey = f"col_{col}_val{val}"
                boxKey = f"box_{col // 3}_{row // 3}_val{val}"

                if rowKey in seen or colKey in seen or boxKey in seen:
                    return False
                
                seen.add(rowKey)
                seen.add(colKey)
                seen.add(boxKey)

        return True