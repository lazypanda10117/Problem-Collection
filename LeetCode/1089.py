from collections import deque

class Solution:    
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = deque([])
        for idx, n in enumerate(arr):
            if n == 0:
                queue.append(0)
            queue.append(n)
            arr[idx] = queue.popleft()
