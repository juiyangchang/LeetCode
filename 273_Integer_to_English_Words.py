class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        one_to_19 = 'One Two Three Four Five Six Seven Eight Nine Ten ' \
                    'Eleven Twelve Thirteen Fourteen Fifteen Sixteen ' \
                    'Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousands = 'Thousand Million Billion'.split()

        def convert_below_thousand(num):
            '''
            Convert any number from 1 to 999 to Words
            '''
            ret = []
            # Convert num % 100 to words
            if 0 < (num % 100) < 20:
                ret.append(one_to_19[(num % 100) - 1]);
            elif (num % 100) > 19:
                if num % 10 != 0:
                    ret.append(one_to_19[(num % 10) - 1])
                # Tens starts counting from Twenty, thus -2
                ret.append(tens[((num % 100) // 10) - 2])

            # Convert num // 100 to words
            if (num // 100) > 0:
                ret.extend(['Hundred', one_to_19[(num // 100) - 1]])

            return ret

        ret = []
        ctr = 0

        while num:
            num, res = num // 1000, num % 1000
            ret.extend(convert_below_thousand(res))
            if num > 0:
                if num % 1000 > 0:
                    # if the number remaining is between one million and one thousand, add a word in the thousands
                    ret.append(thousands[ctr])
                # Add Million (ctr = 1) or Billion (ctr = 2)
                ctr += 1

        return ' '.join(ret[::-1])
