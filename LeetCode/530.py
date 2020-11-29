class Solution:
    LEFT = 0
    RIGHT = 1
    
    ODD = 1
    EVEN = 0
    
    def giveParity(self, num: int) -> int:
        return num % 2
    
    def isMiddleSingle(self, nums: List[int]):
        return nums[0] != nums[1] and nums[1] != nums[2] and nums[2] != nums[0]
        
    def getDirection(self, idx: int, nums: List[int]):
        if self.giveParity(idx) == self.ODD:
            if nums[1] == nums[2]:
                return self.LEFT
            else:
                # This imples from previous code that nums[0] == nums[1] as we do the isSingle check before
                return self.RIGHT
        else:
            if nums[0] == nums[1]:
                return self.LEFT #because if they are different, it means the single index did not affect this
            else:
                return self.RIGHT
            
    def singleDirection(self, idx: int, nums: List[int]):
        if idx >= 1 and idx <= len(nums) - 2:
            leftIdx = (int)(idx - 1)
            rightIdx = (int)(idx + 2)
            tempNums = nums[leftIdx: rightIdx]
            isSingle = self.isMiddleSingle(tempNums)
            return (isSingle, self.LEFT) if isSingle else (isSingle, self.getDirection(idx, tempNums))
        elif idx >= 1:
            # Should not be able to reach here unless the single element is here
            return (True, self.RIGHT)
        elif idx <= len(nums) - 2:
            # Should not be able to reach here unless the single element is here
            return (True, self.LEFT)
        else:
            raise "HOW DO YOU EVEN GET TO THIS CONDITION???"
            
    # Need to check for some edge cases (literally on the edge lol)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search on list, determine direction
        n = len(nums) - 1 # Must be even, since number of elements is odd
        left = 0
        right = n

        while left < right:
            idx = (int)((left + right) / 2)
            sd = self.singleDirection(idx, nums)
            if sd[0]:
                return nums[idx]
            else:
                if sd[1] == self.LEFT:
                    right = idx - 1
                else:
                    left = idx + 1

        return nums[left]
