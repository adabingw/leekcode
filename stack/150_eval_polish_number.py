class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                elif token == '/':
                    if num1 * num2 > 0:
                        res = math.floor(float(num1) / float(num2))
                    else:
                        res = math.ceil(float(num1) / float(num2))
                stack.append(int(res))
            else: 
                stack.append(int(token))
        return stack[0]
