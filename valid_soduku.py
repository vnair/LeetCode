class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        dict_row = list()
        dict_col = list()
        dict_grid = list()
        for i in xrange(0,9):
            dict_row.append({})
            dict_col.append({})
        for i in xrange(0,9):
            for j in xrange(0,9):
                if board[i][j] in dict_row[i]:
                    return False
                elif board[i][j] != '.':
                    dict_row[i][board[i][j]]=True   
                if board[j][i] in dict_col[i]:  
                    return False
                elif board[j][i] != '.':    
                    dict_col[i][board[j][i]]=True
        for i in xrange(0,9,3):
            for j in xrange(0,9,3):
                d = dict()
                for k in xrange(0,3):
                    for l in xrange(0,3):
                        if board[i+k][j+l] in d:
                            print i+k,j+l
                            return False
                        elif board[i+k][j+l] != '.':    
                            d[board[i+k][j+l]]=True
        return True
            

