class Solution:
    # I JUST WANT TO DO A RECURSIVE SOLUTION!!!
    
    def getLen(self, num):
        s_len = 0
        while (int) (num / (10 ** s_len)) != 0:
            s_len += 1
        return s_len
            
    def getDigit(self, num, idx):
        return (int)(num/(10**idx) % 10)

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_len = self.getLen(x) - 1
        idx = 0
        while idx < (int)((x_len+1)/2):
            if self.getDigit(x, idx) != self.getDigit(x, x_len - idx):
                return False
            idx += 1
        return True
