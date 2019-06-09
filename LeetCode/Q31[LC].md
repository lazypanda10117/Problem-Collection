# Question 31 LC

### Question Details:
> Question ID: 31
> 
> Question Name: Next Permutation
> 
> Question Description: Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
> 
> If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
> 
> Question Note: The replacement must be in-place and use only constant extra memory.
> 
> Question Difficulty: Medium
> 
> Question Example:
> 
> ```
> 1,2,3 → 1,3,2
> 3,2,1 → 1,2,3
> 1,1,5 → 1,5,1
> ``` 
> Question Reference: [Question 31 Link](https://leetcode.com/problems/next-permutation/)


### Solution Details
__Solution Statistics__:
> Runtime: 36 ms [98.30%]
> 
> Memory: 131 mb [87.66%]

__Solution Main Idea__:
> Main Idea is to swap the first element that doesnt follow the increasing (right to left) order and swap it with the next smallest element in the elements traversed that is bigger than the element in conflict

__Solution Analysis__:
> Runtime Analysis: O(n) as it at most traverses the list 2 times. One for finding the element in conflict and the other for in place swapping.
> 
> Auxillary Space Analysis: O(1) because we do in place swapping for resorting the elements after the element in conflict

__Solution Implementation__:

```python
class Solution:
    def findSmallestLargerThanK(self, nums: List[int], k: int):
        idx = len(nums) - 1
        while idx >= 0:
            if nums[idx] > k:
                # print("Target: " + str(k))
                # print("Nums: " + str(nums[idx]))
                # print("Idx: " + str(idx))
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
```