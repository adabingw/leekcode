class Node:
    def __init__(self):
        self.children = [ None ] * 10

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, num):
        node = self.root
        num_str = str(num)
        for digit in num_str:
            i = int(digit)
            if not node.children[i]:
                node.children[i] = Node()
            node = node.children[i]
    
    def find_longest_prefix(self, num):
        node = self.root
        num_str = str(num)
        res = 0
        for digit in num_str:
            i = int(digit)
            if node.children[i]:
                res += 1
                node = node.children[i]
            else:
                break
        return res

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        trie = Trie()

        for a in arr1:
            trie.insert(a)
        
        res = 0

        for a in arr2:
            res = max(res, trie.find_longest_prefix(a))
        
        return res