class Solution:
    def numSteps(self, s: str) -> int:
        counter = 0
        while not s == "1":
            if s[-1] == "1":
                # odd
                b = False
                for i in range(1,len(s)+1):
                    if s[-i] == "0":
                        # to 1
                        s = s[:-i] + self.invert(s[-i:])
                        b = True
                        break
                if not b:
                    s = "1" + self.invert(s)
            else:
                # even
                s = s[:-1]
            counter += 1
        return counter
    
    def invert(self, lst):
        result = ""
        for s in lst:
            if s == "0":
                result += "1"
            else:
                result += "0"
        return result
