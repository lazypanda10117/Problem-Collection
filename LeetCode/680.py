class Solution:
    def remove_direction(self, s, left):
        removed, success = False, True
        cur_left, cur_right = 0, len(s)-1
        # remove right
        while True:
            if cur_left > cur_right:
                break
            if not s[cur_left] == s[cur_right]:
                if not removed:
                    removed = True
                    if left:
                        cur_left += 1 
                    else:
                        cur_right -= 1
                else:
                    if success:
                        success = False
                    else:
                        break
            else:
                cur_left += 1
                cur_right -= 1
        if success:
            return True
        return False
        
    def validPalindrome(self, s: str) -> bool:
        return self.remove_direction(s, True) or self.remove_direction(s, False)
