class Solution:
    def valid(self, m:List[List[str]])-> bool:
        res = True
        s = set()
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] != '.':
                    if m[i][j] in s:
                        return False
                    else:
                        s.add(m[i][j])
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        
        r = 0
        c = 0

        #check first block is valid or not 
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sliced = [row[c:c+3] for row in board[r:r+3]]
                res = res & self.valid(sliced)
                if res==False:
                    return False
        #check for each row 
        for r in range(0,9):
            sliced = [board[r:r+1]]
            res = res & self.valid(board[r:r+1][:])
            if res==False:
                return False
        for c in range(0,9):
            sliced = [row[c:c+1] for row in board[:]]
            res = res & self.valid(sliced)
            if res==False:
                return False

        #check for each column
        return True
        