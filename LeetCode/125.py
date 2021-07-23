class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c
        new_string = new_string.lower()
        for i in range(len(new_string) // 2):
            if not new_string[i] == new_string[-(i+1)]:
                return False
        return True