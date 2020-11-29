class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        idx = 0 
        while idx <= len(arr)-3:
            if (arr[idx] % 2 and arr[idx+1] % 2 and arr[idx+2] % 2):
                return True
            idx += 1
        return False
