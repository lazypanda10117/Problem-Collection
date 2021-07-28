class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = []
        carry = 1
        for d in digits[::-1]:
            result = (d + carry) % 10
            carry =  (d + carry) // 10
            new_digits.append(result)
        if carry:
            new_digits.append(carry)
        return new_digits[::-1]
