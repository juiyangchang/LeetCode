class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        if (numerator < 0) != (denominator < 0):
            sgn = True
        else:
            sgn = False           
            
        numerator, denominator = abs(numerator), abs(denominator)
        
        lookup = {}
        quotient, remainder = numerator // denominator, numerator % denominator
        
        if remainder == 0:
            return '-' + str(quotient) if sgn else str(quotient)
        
        int_quotient = quotient
        
        fraction = []
        while remainder not in lookup and remainder != 0:
            lookup[remainder] = len(fraction)
            remainder *= 10
            quotient, remainder = remainder // denominator, remainder % denominator
            fraction.append(quotient)
            
        if remainder == 0:
            return ''.join(map(str, ['-' if sgn else ''] + [int_quotient] + ['.'] + fraction))
        else:
            return ''.join(map(str, ['-' if sgn else ''] + [int_quotient] + ['.'] + fraction[:lookup[remainder]] + ['('] + 
                       fraction[lookup[remainder]:] + [')']))