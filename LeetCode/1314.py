class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        dp = [[-1 for _ in r] for r in mat]
        
        # base case
        base_sum = 0
        for i in range(k+1):
            for j in range(k+1):
                if i < len(mat) and j < len(mat[0]):
                    base_sum += mat[i][j]
        dp[0][0] = base_sum
        
        # doing the base column
        for i in range(1, len(mat)):
            new_sum = dp[i-1][0]
            if i - k > 0:
                new_sum -= sum(mat[i-k-1][0:k+1])
            if i + k < len(mat):
                new_sum += sum(mat[i+k][0:k+1])
            dp[i][0] = new_sum
        
        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                # sliding each row
                new_sum = dp[i][j-1]
                if j - k > 0:
                    new_sum -= sum([mat[r][j-k-1] for r in range(max(0, i-k), min(i+k+1, len(mat)))])
                if j + k < len(mat[0]):
                    new_sum += sum([mat[r][j+k] for r in range(max(0, i-k), min(i+k+1, len(mat)))]) 
                dp[i][j] = new_sum

        return dp
