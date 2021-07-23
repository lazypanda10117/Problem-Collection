class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            val = nums[mid]
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
