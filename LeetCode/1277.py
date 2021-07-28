class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[[0,0,0, 0] for _ in range(len(matrix[i]))] for i in range(len(matrix))]
        
        # i = for the 0 case, j for the 1 case, k ,l
        # i = number of submatrix of all ones with right lower endpoint there
        # j = number of 1 matrices that can be generated from the left diagonal
        # k = how many consecutive to the left (including self)
        # l = how many consecutive to the top (including self)
        
        # base case for i,j = 0,0
        dp[0][0][0] = matrix[0][0]
        dp[0][0][1] = matrix[0][0]
        dp[0][0][2] = matrix[0][0]
        dp[0][0][3] = matrix[0][0]
        
        # base case for first row
        for j in range(1, len(matrix[0])):
            dp[0][j][0] = dp[0][j-1][0] + matrix[0][j]
            dp[0][j][1] = matrix[0][j]
            dp[0][j][2] = dp[0][j-1][2] + 1 if matrix[0][j] == 1 else 0
            dp[0][j][3] = dp[0][j-1][3] + 1 if matrix[0][j] == 1 else 0

        # base case for first col
        for i in range(1, len(matrix)):
            dp[i][0][0] = dp[i-1][0][0] + matrix[i][0]
            dp[i][0][1] = matrix[i][0]
            dp[i][0][2] = dp[i-1][0][3] + 1 if matrix[i][0] == 1 else 0
            dp[i][0][3] = dp[i-1][0][3] + 1 if matrix[i][0] == 1 else 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    dp[i][j][0] = dp[i-1][j][0] + dp[i][j-1][0] - dp[i-1][j-1][0]
                    dp[i][j][1] = 0
                    dp[i][j][2] = 0
                    dp[i][j][3] = 0
                else:
                    old_squares = dp[i-1][j][0] + dp[i][j-1][0] - dp[i-1][j-1][0]
                    new_squares = min(dp[i-1][j-1][1], dp[i][j-1][2], dp[i-1][j][3]) + 1 
                    # print(f"NEW SQUARES: {new_squares}, {i,j}")
                    dp[i][j][0] = old_squares + new_squares
                    dp[i][j][1] = new_squares
                    dp[i][j][2] = dp[i][j-1][2] + 1
                    dp[i][j][3] = dp[i-1][j][3] + 1
        
        # print(dp)
        return dp[-1][-1][0]
