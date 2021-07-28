class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        flip = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        new_num = ''
        for s in num[::-1]:
            if s not in flip:
                return False
            new_num += flip[s]
        return new_num == num
