class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_arr = nums.sort()
        i = 1
        while i < len(nums):
            # swap i with i + 1
            temp = nums[i]
            if i+1 < len(nums):
                nums[i] = nums[i+1]
                nums[i+1] = temp
            i += 2
