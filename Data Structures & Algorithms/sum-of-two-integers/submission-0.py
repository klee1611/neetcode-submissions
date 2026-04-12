class Solution:
    def getSum(self, a: int, b: int) -> int:
        r = 0
        carry = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            cur_bit = a_bit ^ b_bit ^ carry
            if a_bit & b_bit or a_bit & carry or b_bit & carry:
                carry = 1
            else:
                carry = 0
            
            if cur_bit:
                r |= (1 << i)

        if r > 0x7FFFFFFF:
            r = ~(r ^ 0xFFFFFFFF)

        return r