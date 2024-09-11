class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        stack = []
        k = []
        curr_string = ''
        curr_digit = ''
        for i, v in enumerate(s):
            if v.isdigit():
                curr_digit += v
            elif v == '[':
                k.append(int(curr_digit))
                stack.append('')
                curr_digit = ''
                if curr_string:
                    stack[-1] = curr_string
                    curr_string = ''
            elif v == ']':
                k_ = k.pop()
                string = curr_string * k_
                if stack:
                    string0 = stack.pop()
                    curr_string = string0 + string
                else:
                    res += string
                    curr_string = ''
            else:
                curr_string += v
        res += curr_string
        return res