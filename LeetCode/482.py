class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        str_join = ''.join(s.upper().split('-'))
        new_str = ''
        for idx, c in enumerate(str_join[::-1]):
            if idx != 0 and idx % k == 0:
                new_str += '-'
            new_str += c
        return new_str[::-1]
