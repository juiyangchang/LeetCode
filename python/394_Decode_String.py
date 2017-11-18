class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        str_stack = []
        rep_count, buffer, res = 1, '', ''
        pre_pos = -1

        for i, c in enumerate(s):
            if not str.isdigit(c):
                if c == '[':
                    str_stack.append((rep_count, buffer))
                    buffer = ''
                    rep_count = int(s[pre_pos+1:i])
                elif c == ']':
                    tmp = buffer * rep_count

                    if str_stack:
                        rep_count, buffer = str_stack.pop()
                        buffer += tmp
                    else:
                        res += buffer
                        buffer = ''

                else:
                    buffer += c

                pre_pos = i

        return res + buffer
