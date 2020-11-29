class Solution:
    def findSmallestLargerThanK(self, nums: List[int], k: int):
        idx = len(nums) - 1
        while idx >= 0:
            if nums[idx] > k:
                return idx
            idx -= 1
        return -1
    
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                # Swap with the smallest element
                swap_idx = i + self.findSmallestLargerThanK(nums[i:], nums[i-1])
                tmp = nums[i-1]
                nums[i-1] = nums[swap_idx]
                nums[swap_idx] = tmp
                break
            i -= 1
        # swap the whole list from i to len(nums) - 1
        j = i
        while j < (len(nums) + i) / 2:
            tmp = nums[j]
            nums[j] = nums[(len(nums) - 1 - j + i)] 
            nums[(len(nums) - 1 - j + i)] = tmp
            j += 1
