class Solution:
    def add(self, num1, num2):
        short_num, long_num = (num1, num2) if len(num1) < len(num2) else (num2, num1)
        short_num = short_num[::-1]
        long_num = long_num[::-1]
        result = ''
        carry = 0
        for idx, s in enumerate(long_num):
            if idx >= len(short_num):
                new_num = int(long_num[idx]) + carry
            else:
                new_num = int(short_num[idx]) + int(long_num[idx]) + carry
            carry = new_num // 10
            new_digit = new_num % 10
            result = result + str(new_digit)
        if carry:
            result = result + str(carry)
        return result[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        # for c in num1:
        #     n = int(c)
        # 123 -> 321
        # 456 -> 654
        # 
        if num1 == '0' or num2 == '0':
            return '0'
        
        to_add = []
        short_num, long_num = (num1, num2) if len(num1) < len(num2) else (num2, num1)
        short_num = short_num[::-1]
        long_num = long_num[::-1]

        for idx1, n1 in enumerate(short_num):
            carry = 0
            result = ''
            for idx2, n2 in enumerate(long_num):
                new_num = int(n1) * int(n2) + carry
                carry = new_num // 10
                new_digit = new_num % 10
                result = result + str(new_digit)
            if carry:
                result = result + str(carry)  
            result_pad = f'{result[::-1]}{"0"*idx1}'
            to_add.append(result_pad)
        
        result = '0'
        for num in to_add:
            result = self.add(num, result)
        
        return result