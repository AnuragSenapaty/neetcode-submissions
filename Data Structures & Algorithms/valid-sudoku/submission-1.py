class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        for i in range(9):
            cols.append(set())
        
        rows = []
        for i in range(9):
            rows.append(set())
        
        quad = []
        for i in range(9):
            quad.append(set())
        
        '''
        i 0-2, j0-2 = 0
        i 3-5, j0-2 = 1
        i 6-8, j0-2 = 2

        '''
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in rows[i]) or (board[i][j] in cols[j]):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                
                if i in (0, 1, 2):
                    if j in (0, 1, 2):
                        if board[i][j] in quad[0]:
                            return False
                        else:
                            quad[0].add(board[i][j])
                    elif j in (3, 4, 5):
                        if board[i][j] in quad[1]:
                            return False
                        else:
                            quad[1].add(board[i][j])
                    elif j in (6, 7, 8):
                        if board[i][j] in quad[2]:
                            return False
                        else:
                            quad[2].add(board[i][j])
                if i in (3, 4, 5):
                    if j in (0, 1, 2):
                        if board[i][j] in quad[3]:
                            return False
                        else:
                            quad[3].add(board[i][j])
                    elif j in (3, 4, 5):
                        if board[i][j] in quad[4]:
                            return False
                        else:
                            quad[4].add(board[i][j])
                    elif j in (6, 7, 8):
                        if board[i][j] in quad[5]:
                            return False
                        else:
                            quad[5].add(board[i][j])
                if i in (6, 7, 8):
                    if j in (0, 1, 2):
                        if board[i][j] in quad[6]:
                            return False
                        else:
                            quad[6].add(board[i][j])
                    elif j in (3, 4, 5):
                        if board[i][j] in quad[7]:
                            return False
                        else:
                            quad[7].add(board[i][j])
                    elif j in (6, 7, 8):
                        if board[i][j] in quad[8]:
                            return False
                        else:
                            quad[8].add(board[i][j])
        
        return True


        