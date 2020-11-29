class Solution:
    def reformat(self, s: str) -> str:
        result = sorted(s)
        idx = 0
        stop = 0
        while idx < len(result):
            if str(result[idx]) not in ['0','1','2','3','4','5','6','7','8','9']:
                stop = idx
                break
            idx += 1
        i_arr = result[:stop]
        s_arr = result[stop:]

        rs = ''
        if len(i_arr) not in [len(s_arr)-1, len(s_arr), len(s_arr)+1]:
            return rs
        
        if len(i_arr) < len(s_arr):
            rs += s_arr.pop()
            l = False
        else:
            rs += i_arr.pop()
            l = True

        while len(i_arr) > 0 or len(s_arr) > 0:
            if l:
                rs += s_arr.pop()
                l = False
            else:
                l = True
                rs += i_arr.pop()
        return rs
