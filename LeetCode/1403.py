class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        sumN = sum(nums)
        tempN = 0
        tempN2 = sumN
        for i in range(1,len(nums)+1):
            tempN += nums[-i]
            tempN2 -= nums[-i]
            if tempN > tempN2:
                result = nums[-i:]
                result.reverse()
                return result
