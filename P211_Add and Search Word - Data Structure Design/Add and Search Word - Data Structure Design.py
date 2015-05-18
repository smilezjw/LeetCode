# coding=utf8

__author__ = 'smilezjw'


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # add a word into the data structure
    def addWord(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        return self.find(self.root, word)

    def find(self, node, word):
        if word == '':
            return node.isWord
        if word[0] == '.':
            for key in node.children:
                if self.find(node.children[key], word[1:]):
                    return True
        else:
            child = node.children.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False

###################################################################################
# 这道题要求实现一个具有字符串检索功能的词典，使用Trie树，正好P208实现了Trie树。
# 在检索字符串时，如果该字符串含有通配符.则需要用递归匹配当前层的所有节点，并向下
# 检索多个路径。
#