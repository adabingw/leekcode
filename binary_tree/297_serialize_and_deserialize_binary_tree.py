# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    """
    preorder traversal: visit node before visiting left and right trees
    - use FLAG to indicate null values
    - to serialize: if not None (FLAG), append current node,
      then recurse to left tree, then recurse to right tree
    - to deserialize: if not None (RET), create node,
      then create left node, then create right node
    """

    FLAG = "_"

    def serialize_(self, node, arr):
        """
        node: TreeNode
        arr: str[]
        """
        if node is None:
            arr.append(self.FLAG)
            return
        
        arr.append(str(node.val))

        self.serialize_(node.left, arr)
        self.serialize_(node.right, arr)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.serialize_(root, res)
        return ','.join(res)

    def deserialize_(self, data):
        """
        data: str[]
        """
        v = data.pop(0)

        if v == self.FLAG:
            return None
        
        node = TreeNode(int(v))
        node.left = self.deserialize_(data)
        node.right = self.deserialize_(data)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        return self.deserialize_(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))