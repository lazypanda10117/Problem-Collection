class TrieNode:
    def __init__(self):
        self.end = False
        self.child = dict()
    
class Solution:
    def dfs(self, board, start, trie, stack):
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        x,y = start

        # check in boundary
        if not(x >= 0 and x < len(board)):
            return False
        if not(y >= 0 and y < len(board[0])):
            return False
        
        c = board[x][y]
        if c not in trie.child:
            return False
        board[x][y] = '?'
        
        new_trie = trie.child[c]
        new_stack = stack + c

        if new_trie.end:
            new_trie.end = False
            self.result.append(new_stack)
        
        for d in DIR:
            self.dfs(board, (x+d[0], y+d[1]), new_trie, new_stack) 
        
        board[x][y] = c
    
    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.child:
                    cur.child[c] = TrieNode()
                cur = cur.child[c]
            cur.end = True
        return root
    
       
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = []
        root = self.build_trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, (i,j), root, "")
        return self.result