class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num_map = dict(
            IV=4,
            IX=9,
            XL=40,
            XC=90,
            CD=400,
            CM=900,
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )
        
        idx = 0
        s_len = len(s)
        result = 0
        
        while idx < s_len:
            if s_len - idx > 1:
                roman_2_digi = roman_num_map.get(s[idx:idx+2])
                if roman_2_digi is None:
                    result += roman_num_map.get(s[idx:idx+1])
                    idx += 1
                else:
                    result += roman_2_digi
                    idx += 2
            else:
                result += roman_num_map.get(s[idx:idx+1])
                break

        return result
