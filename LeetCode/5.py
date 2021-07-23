class Solution:
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False
        
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)+1):
            for j in range(i+1):
                substr = s[j:len(s)-i+j]
                if self.isPalindrome(substr):
                    return substr
        return ""