class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[0 for r in range(len(matrix[0]))] for x in range(len(matrix))]

        r = len(matrix)
        c = len(matrix[0])
        self.prefixSum[0][0] = matrix[0][0]
        for cc in range(1, c):
            self.prefixSum[0][cc]= self.prefixSum[0][cc-1]+matrix[0][cc]

        for rr in range(1,r):
            self.prefixSum[rr][0] = self.prefixSum[rr-1][0]+matrix[rr][0]

        for rr in range(1,r):
            for cc in range(1,c):
                self.prefixSum[rr][cc] = self.prefixSum[rr][cc-1]+self.prefixSum[rr-1][cc]-self.prefixSum[rr-1][cc-1]+ matrix[rr][cc]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        if col1-1>=0 and row1-1>=0:
            ans = self.prefixSum[row2][col2]-self.prefixSum[row2][col1-1]-self.prefixSum[row1-1][col2]+self.prefixSum[row1-1][col1-1]      
        elif col1-1>=0:
            ans = self.prefixSum[row2][col2]-self.prefixSum[row2][col1-1]
        elif row1-1>=0:
            ans = self.prefixSum[row2][col2]-self.prefixSum[row1-1][col2]
        else:
            ans = self.prefixSum[row2][col2]
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)