class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(0, 9):
            freq_dict = {}
            for j in range(0, 9):
                if board[i][j].isdigit():
                    if board[i][j] in freq_dict:
                        return False
                    freq_dict[board[i][j]] = 1

        for i in range(0, 9):
            freq_dict = {}
            for j in range(0, 9):
                if board[j][i].isdigit():
                    if board[j][i] in freq_dict:
                        return False
                    freq_dict[board[j][i]] = 1

        for i in range(0, 3):
            for j in range(0, 3):
                freq_dict = {}
                for l in range(0 ,3):
                    for c in range(0, 3):
                        if board[l + 3 * i][c + 3 * j].isdigit():
                            if board[l + 3 * i][c + 3 * j] in freq_dict:
                                return False
                            freq_dict[board[l + 3 * i][c + 3 * j]] = 1

        return True