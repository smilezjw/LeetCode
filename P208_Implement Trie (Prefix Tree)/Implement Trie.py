# coding=utf8

__author__ = 'smilezjw'


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # return void, insert a word into the trie
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    # return boolean, return if the word is in the trie
    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if not node:
                return False
        return node.isWord

    # return boolean, return if there is any word in the trie that starts with the given prefix
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return False
        return True