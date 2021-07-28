class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # base_i = -math.inf()
        last_num = nums[0]
        cur_len = 1
        max_len = 0
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
        max_len = max(max_len, cur_len)
        return max_len