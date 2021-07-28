from collections import defaultdict, deque
from copy import deepcopy

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def preprocess(s):
            # get a map of how many of each alphabet is after this index 
            # build backward
            result = []
            last_char_count = defaultdict(deque)
            for idx in reversed(range(len(s))):
                c = s[idx]
                new_char_count = deepcopy(last_char_count)
                new_char_count[c].appendleft(idx)
                last_char_count = new_char_count
                result.append(new_char_count)
            return result[::-1]
        
        count = 0
        cur_idx = 0
        processed_s = preprocess(source)
        # print(processed_s)

        for c in target:                
            if cur_idx < len(source) and c in processed_s[cur_idx]:
                new_idx_list = processed_s[cur_idx][c]
                next_idx = new_idx_list[0] + 1
                cur_idx = next_idx
            else:
                # not in cur_idx
                cur_idx = 0
                if c in processed_s[cur_idx]:
                    new_idx_list = processed_s[cur_idx][c]
                    next_idx = new_idx_list[0] + 1
                    cur_idx = next_idx
                    count += 1
                else:
                    return -1
        count += 1
        return count