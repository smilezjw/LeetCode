# coding=utf8

__author__ = 'smilezjw'


class MinStack:
    # 双栈法，开辟两个栈
    def __init__(self):
        self.stack = []      # 普通的栈，进行入栈出栈操作
        self.minStack = []   # 栈顶记录所有元素中的最小元素

    def push(self, x):      # 入栈操作
        self.stack.append(x)
        # 如果入栈的元素是当前元素中的最小元素，则还要入最小栈中
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):          # 出栈操作
        x = self.stack.pop()
        # 如果出栈的元素是当前元素中的最小元素，则最小栈弹出该元素
        if x == self.minStack[-1]:
            self.minStack.pop()

    def top(self):         # 取得栈顶元素
        return self.stack[-1]

    def getMin(self):      # 最小栈的栈顶记录最小元素，常数时间即可取得该元素
        return self.minStack[-1]

#######################################################################################
# 这道题采用双栈法，开辟两个栈（用列表来表示），stack中存储当前所有元素，minStack中存储
# 当前最小值，能够在常数时间内取得最小值。
# 注意在入栈和出栈时要判断minStack的栈顶元素。
#