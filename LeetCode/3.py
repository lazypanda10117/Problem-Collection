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
