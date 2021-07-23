class Solution:
    def getRow(self, board, idx):
        return board[idx]
    
    def getCol(self, board, idx):
        res = []
        for row in board:
            res.append(row[idx])
        # print(f"COL {idx}",  res)
        return res
    
    def getBox(self, board, idx):
        # (0,0) (1,0) (2,0)
        # 3 4 5
        # 6 7 8
        x, y = idx
        res = []
        for i in range(3):
            for j in range(3):
                res.append(board[x*3+i][y*3+j])
        return res        
    
    def has_duplicates(self, lst):
        for i in range(1,10):
            if lst.count(str(i)) > 1:
                return True
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
        rows = [i for i in range(9)]
        cols = [i for i in range(9)]
        
        for b in boxes:
            if self.has_duplicates(self.getBox(board, b)):
                return False
        
        for r in rows:
            if self.has_duplicates(self.getRow(board, r)):
                return False
        
        for c in cols:
            if self.has_duplicates(self.getCol(board, c)):
                return False
        
        return True