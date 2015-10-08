# coding=utf8

__author__ = 'smilezjw'


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.elem = None  # 引入变量缓存预先获取的下一个元素

    def peek(self):
        if self.elem:    # 只有next()被调用之后，peek才能返回下一个元素，否则只能返回预先获取的元素
            return self.elem
        elif self.iterator.hasNext():
            self.elem = self.iterator.next()
            return self.elem
        return 0

    def next(self):
        if self.elem:
            val = self.elem
            self.elem = None
            return val
        return self.iterator.next()

    def hasNext(self):
        return (self.elem is not None) or self.iterator.hasNext()
