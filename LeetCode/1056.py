class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        str_num = str(n)
        new_num = ''
        for c in str_num:
            if c in rotation_map:
                new_num += str(rotation_map[c])
            else:
                return False
        return new_num[::-1] != str_num