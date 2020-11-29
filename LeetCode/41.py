class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        idx = 0
        while idx < size:
            num = nums[idx]
            # Swappinag to the right index
            if 1 <= num and num <= size:
                tmp = nums[num-1]
                if not (tmp == nums[idx]):
                    nums[num-1] = num
                    nums[idx] = tmp
                    idx -= 1
            idx += 1
                
        for idx, num in enumerate(nums):
            if idx != num - 1:
                return idx + 1 

        return size + 1
