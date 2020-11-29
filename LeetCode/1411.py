class Solution:
    def numOfWays(self, n: int) -> int:
        modu = 10**9+7
        ways = 12
        i = 1
        D = 6
        U = 6
        while i < n:
            preD = D
            D = D * 3 + U * 2
            U = preD * 2 + U * 2 
            ways = D + U
            ways %= modu
            i += 1
        return ways
