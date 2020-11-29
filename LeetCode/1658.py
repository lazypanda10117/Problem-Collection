class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if len(nums) == 1 and x == nums[0]:
            return 1
        
        DP = dict()
        sum = 0
        res = 1000000001 # > contraints        
        cur = 0
        
        for idx, i in enumerate(reversed(nums)):
            DP[sum] = idx
            sum += i
            if sum > x:
                break

        for idx, i in enumerate(nums):
            if x - cur in DP and DP[x-cur] + idx <= len(nums):
                res = min((idx) + DP[x-cur], res)
            cur += i
            if cur > x:
                break

        return -1 if res == 1000000001 else res
