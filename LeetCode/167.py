class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = 0
        end = len(numbers) - 1
        while (start < end):
            tempRes = numbers[start] + numbers[end]
            if tempRes > target:
                end -= 1
            elif tempRes < target:          
                start += 1
            else:
                return [start+1, end+1]
