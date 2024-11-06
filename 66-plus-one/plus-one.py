class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        i = len(digits)-1
        carry = 1

        while i >= 0 and carry:
            if digits[i] == 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
            i -= 1

        if carry:
            digits.append(carry)
            digits = digits[-1:] + digits[:-1]
            
        return digits 