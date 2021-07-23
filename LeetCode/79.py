class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, (i,j), word, set()):
                    return True
        return False
    
    def dfs(self, board, start, word, visited):
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        x,y = start

        # check in boundary
        if not(x >= 0 and x < len(board)):
            return False
        if not(y >= 0 and y < len(board[0])):
            return False
        
        # check not visited
        if (x,y) in visited:
            return False
        
        if not board[x][y] == word[0]:
            return False
        
        # last character is matching
        if len(word) == 1:
            return True
        
        visited.add((x,y))
        
        result = False
        for d in DIR:
            result = result or self.dfs(board, (x+d[0], y+d[1]), word[1:], visited) 
        
        visited.remove((x,y))
        return result