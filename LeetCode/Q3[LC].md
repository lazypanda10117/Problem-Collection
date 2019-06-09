# Question 3 LC

### Question Details:
> Question ID: 3
> 
> Question Name: Longest Substring Without Repeating Characters
> 
> Question Description: Given a string, find the length of the longest substring without repeating characters.
> 
> Question Note: N/A
> 
> Question Difficulty: Medium
> 
> Question Example:
> 
> ```
> Input: "abcabcbb"
> Output: 3 
> Explanation: The answer is "abc", with the length of 3. 
> ```
> ```
> Input: "bbbbb"
> Output: 1
> Explanation: The answer is "b", with the length of 1.
> ```
> ```
> Input: "pwwkew"
> Output: 3
> Explanation: The answer is "wke", with the length of 3. 
> Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
> ``` 
> Question Reference: [Question 3 Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)


### Solution Details
__Solution Statistics__:
> Runtime: 56 ms [97.27%]
> 
> Memory: 13.1 mb [91.53%]

__Solution Main Idea__:
> The main idea of this solution is similar to that of Boyer Moore bad character herustic.

__Solution Analysis__:
> Runtime Analysis: O(n) as it traverses the string only once and all operations during traversal are constant time
> 
> Auxillary Space Analysis: Worst Case O(n) due to the temp_dict storing characters in the string

__Solution Implementation__:

```python
class Solution:
    # Idea similar to boyer moore bad character heruistic
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_dict= dict()
        max_len = 0
        cur_len = 0
        cur_idx = 0
        for idx, c in enumerate(s):
            if c in temp_dict and temp_dict[c] >= cur_idx:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = idx - temp_dict[c]
                cur_idx = temp_dict[c]
            else:
                cur_len += 1
            temp_dict[c] = idx
                
        return cur_len if cur_len > max_len else max_len
```

__Solution Archive__:

Version 1:

> Runtime: 428 ms [18.77%]
> 
> Memory: 13.3 mb [56.23%]

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_dict= dict()
        max_len = 0
        cur_len = 0
        # cur_idx = 0
        for idx, c in enumerate(s):
            if c in temp_dict: #and temp_dict[c] > cur_idx:
                max_len = cur_len if cur_len > max_len else max_len
                # Idea similar to boyer moore bad character heruistic
                cur_len = idx - temp_dict[c]
                # or we can choose to clear everything that comes before c
                # cur_idx = idx
                temp_dict = {key: val for key, val in temp_dict.items() if val > temp_dict[c]}
                temp_dict[c] = idx
            else:
                temp_dict[c] = idx
                cur_len += 1
            # print(cur_len)

        max_len = cur_len if cur_len > max_len else max_len
                
        return max_len
```