# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in xrange(len(tokens)):
            if tokens[i].isdigit() or len(tokens[i]) > 1:  # 判断是否为数字，但是负数不能用isdigit()判断出来，只能通过位数来判断
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(num2 + num1)
                elif tokens[i] == '-':
                    stack.append(num2 - num1)
                elif tokens[i] == '*':
                    stack.append(num2 * num1)
                 # 注意python中的除法是向下取整，因此7 / (-2) = -4，
                 # 这里先化为浮点数进行计算，然后再取整，取整则是直接去掉小数部分，int(2.5) = 2, int(-2.5) = -2
                elif tokens[i] == '/':
                    stack.append(int(num2 * 1.0 / num1))
        return stack[-1]

if __name__ == '__main__':
    s = Solution()
    tokens = ['2', '1', '+', '3', '*']
    tokens2 = ['3', '-4', '+']
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print s.evalRPN(tokens3)

#########################################################################################
# 这道题比较简单，是经典的逆波兰式求值，首先开辟一个空栈，遇到数字则入栈，遇到运算符则将
# 栈顶的两个数字出栈进行运算，并将计算结果入栈，最后栈中只剩下一个数字就是计算结果。
# 在求解过程中有两个地方需要注意：
# 1.用isdigit()判断是否是数字时，只能判断非负数，对于负数是判断不出来的，即'-2'.isdigit()
#   返回False。
# 2.python中的除法运算都是向下取整，即-7 / 2 = -4, 7 / 2 = 3；而C++中除法运算则是向零取整，
#   因此这里先转化为浮点数运算，然后将浮点数转化为整数，取整的过程则是将小数部分直接去掉。
#
#