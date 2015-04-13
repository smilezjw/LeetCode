# coding=utf8

__author__ = 'smilezjw'

import collections

class LRUCache_OrderedDict:
    # python的字典查找元素O(1)时间复杂度，但是字典是无序的。
    # collections.OrderedDict数据类型则是有序的，后加入的元素一定排在先加入元素的后面，其操作和字典类似。
    # 其中方法popitem(last=True)是从OrderedDict中弹出尾部的元素，popitem(last=False)则是弹出头部的元素。
    def __init__(self, capacity):
        self.Dict = collections.OrderedDict()
        self.capacity = capacity
        self.itemsNum = 0

    def get(self, key):
        try:
            value = self.Dict[key]
            del self.Dict[key]
            self.Dict[key] = value
            return value
        except:
            return -1

    def set(self, key, value):
        try:
            # key已经在cache中，需要重新设置key对应的value值
            del self.Dict[key]
            self.Dict[key] = value
            return
        except:
            # key不在cache中，添加新的(key,value)对
            if self.itemsNum == self.capacity:
                # 弹出头部的元素，也就是最先加入的元素
                self.Dict.popitem(last=False)
                self.itemsNum -= 1
            self.Dict[key] = value
            self.itemsNum += 1
            return


# 采用双向链表进行插入、删除，可以灵活地调整次序，时间复杂度为O(1)
class Node:  # 双向链表中节点的定义
    def __init__(self, k, x):
        self.key = k
        self.val = x
        self.prev = None
        self.next = None

class DoubleLinkedList:  # 双向链表有一个表头，其中head指向第一个节点，tail指向最后一个节点
    def __init__(self):
        self.tail = None
        self.head = None

    def isEmpty(self):    # 如果最后一个节点为None，则说明双向链表为空
        return not self.tail

    def removeLast(self):  # 删除tail指向的节点
        self.remove(self.tail)

    def remove(self, node):  # 具体双向链表中删除节点的实现
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.prev.next = node.next
        node.next.prev = node.prev

    def addFirst(self, node):  # 在双向链表的第一个节点前面插入一个新的节点
        if not self.head:       # 如果双向链表为空，则tail和head同时指向新插入的节点
            self.head = self.tail = node
            node.prev = node.next = None
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

class LRUCache_DoubleLinked:
    def __init__(self, capacity):  # 设计LRU cache的数据结构为双向链表
        self.capacity = capacity   # LRU cache容量大小
        self.size = 0              # LRU cache目前占用的容量
        self.hashmap = dict()      # 用hashmap加快搜索，{key:对应节点地址}
        self.cache = DoubleLinkedList()

    def get(self, key):           # 查询操作
        if (key in self.hashmap) and self.hashmap[key]:  # 如果key在字典中说明已经被访问过
            self.cache.remove(self.hashmap[key])    # 那么在双向链表中先删除掉key对应的节点
            self.cache.addFirst(self.hashmap[key])  # 然后将这个节点插入到双向链表表头
            return self.hashmap[key].val            # 返回该节点的值
        else:
            return -1

    def set(self, key, value):    # 更新和插入操作
        if key in self.hashmap:   # 更新操作
            self.cache.remove(self.hashmap[key])    # 先在双向链表中先删除掉key对应的节点
            self.cache.addFirst(self.hashmap[key])  # 然后将这个节点插入到双向链表表头
            self.hashmap[key].val = value           # 修改该节点的值
        else:                     # 插入操作
            node = Node(key, value)                 # 新建一个节点
            self.hashmap[key] = node                # 将key和node的映射关系添加到hashmap中
            self.cache.addFirst(node)               # 将该节点添加到双向链表表头（添加节点都是从头部添加，这样保证最先访问的结点一直在链表的尾部）
            self.size += 1                          # 目前LRU cache中占用容量加1
            if self.size > self.capacity:           # 如果目前LRU cache中占用容量大于缓存的大小
                self.size -= 1
                del self.hashmap[self.cache.tail.key]  # 在hashmap中删除掉最后一个结点的key值和映射关系
                self.cache.removeLast()             # 删除掉双向链表最后一个节点（即最先访问的节点）

##########################################################################################
# 这道题模拟Least Recently Used最近最少使用缓存算法。Python可以用collections.OrderedDict
# 数据类型来模拟缓存中的查询、更新和插入操作，时间复杂度为O(1)。
# 更为朴素的做法是Hashmap和双向链表一起实现缓存中的查询、更新和插入操作。
# 可以参考：http://www.cnblogs.com/zuoyuan/p/3701572.html
#