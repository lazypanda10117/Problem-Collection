class Solution:
    def minOperations(self, n: int) -> int:
        mid = (1 + 2*(n-1) + 1)/2  
        # print(mid)
        j = int(n/2)
        # print(j)
        res = int(j*(j+1)/2) * 2
        if n % 2 == 0:
            res -= j
        return res
