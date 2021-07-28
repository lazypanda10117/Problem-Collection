class Solution:

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        def get_prev_slice(lst, idx):
            if idx <= 0:
                return []
            else:
                if len(lst) >= idx:
                    return lst[:idx]
                return []
        
        def get_post_slice(lst, idx):
            if idx >= len(lst) - 1:
                return []
            else:
                if len(lst) >= idx+1:
                    return lst[idx+1:]
                return []
        
        temp = [(len(s), True, s)]
        for i in range(len(indices)):
            # print("OLD", temp)
            idx = indices[i]
            src_str = sources[i]    
            cur_len = 0
            for t_idx, t in enumerate(temp):
                if cur_len + t[0] > idx:
                    if t[1] and t[2][idx-cur_len:idx+len(src_str)-cur_len] == src_str:
                        # replace with target[i]
                        target = targets[i]
                        temp = temp[:t_idx] + \
                        [(idx-cur_len, True, t[2][:idx-cur_len])] + \
                        [(len(src_str), False, target)] +\
                        [(t[0]-(idx-cur_len+len(src_str)), True, t[2][idx-cur_len+len(src_str):])] + \
                        temp[t_idx+1:]
                    # print("NEW", temp)
                    break
                cur_len += t[0]
        
        new_str = ""
        for t in temp:
            new_str += t[2]
        return new_str
