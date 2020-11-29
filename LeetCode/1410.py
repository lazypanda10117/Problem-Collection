class Solution:
    def entityParser(self, text: str) -> str:
        rd = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        
        for l in [4,5,6,7]:
            i = 0
            dest = len(text)-l
            while i <= dest:
                temp = text[i:i+l]
                if temp in rd:
                    text = text[:i] + rd[temp] + text[i+l:]
                    dest = dest - l + len(rd[temp])
                i += 1
        return text
