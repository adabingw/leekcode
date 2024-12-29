class Node:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = Node()
            curr = curr.children[ord(c) - ord('a')]
        curr.end = True
    
    def shortest_root(self, word):
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c) - ord('a')] is None:
                return word
            curr = curr.children[ord(c) - ord('a')]
            if curr.end:
                return word[:i+1]
        return word

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split(' ')
        trie = Trie()

        for word in dictionary:
            trie.insert(word)
        
        for word in range(len(words)):
            words[word] = trie.shortest_root(words[word])
        
        return ' '.join(words)