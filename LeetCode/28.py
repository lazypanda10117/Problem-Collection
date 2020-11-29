class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Boyer-Moore without Good-Suffix
        if needle == "":
            return 0
        
        hlen = len(haystack)
        nlen = len(needle)
        
        badChar = [-1]*256 
        for i in range(nlen): 
            badChar[ord(needle[i])] = i; 
        
        s = 0
        while (s <= hlen - nlen):
            j = nlen - 1
            while j >= 0 and needle[j] == haystack[s + j]:
                j -= 1
            if j < 0:
                return s
            else:
                s += max(1, j - badChar[ord(haystack[s + j])])
        return -1
