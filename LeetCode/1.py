class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        s_list = list(enumerate(nums))
        s_list.sort(key=(lambda x: x[1]))
        start = 0
        end = len(nums) - 1
        while (start < end):
            tempRes = s_list[start][1] + s_list[end][1]
            if tempRes < target:          
                start += 1
            elif tempRes > target:
                end -= 1
            else:
                return [s_list[start][0], s_list[end][0]]
