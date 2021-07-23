class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        spaces = []
        cur_space = 0
        last_space = False
        for c in s:
            if c == " ":
                cur_space += 1
                last_space = True
            else:
                if last_space:
                    spaces.append(cur_space)
                    last_space = False
                cur_space = 0                            
        if cur_space:
            spaces.append(cur_space)
        else:
            # 0 space in the end
            spaces.append(cur_space)
        
        result = ""
        for idx, w in enumerate(words):
            result += w[::-1]
            result += " " * spaces[idx]
        
        return result