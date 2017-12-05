class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = ((dividend < 0) == (divisor < 0))
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            tmp, inc = divisor, 1
            while dividend >= tmp:
                quotient += inc
                dividend -= tmp
                inc <<= 1
                tmp <<= 1
        if not positive:
            quotient = - quotient
            
        return min(max(-2147483648, quotient), 2147483647)