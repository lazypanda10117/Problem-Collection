class Solution:       
    def numberOfSteps(self, num: int) -> int:
        def recurse_down(n):
            if n == 0:
                return 0
            if n % 2 == 0:
                return 1 + recurse_down(n // 2)
            else:
                return 1 + recurse_down(n - 1)
        return recurse_down(num)