# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_ones(self, root):
        nodes = {}
        def h_one(root):
            nonlocal nodes
            if root is None:
                return False
            has_one = False
            if root.val == 1:
                has_one = True
            left = h_one(root.left)
            right = h_one(root.right)
            has_one = has_one or left or right
            nodes[root] = has_one
            return has_one
        h_one(root)
        return nodes

    def prune_helper(self, root, nodes):
        if not root:
            return
        if root.left and not nodes[root.left]:
            # no ones in left subtree
            root.left = None
        if root.right and not nodes[root.right]:
            # no ones in left subtree
            root.right = None
        self.pruneTree(root.left)
        self.pruneTree(root.right)

    def pruneTree(self, root: TreeNode) -> TreeNode:    
        if not root:
            return None
        nodes = self.build_ones(root)
        if root and not nodes[root]:
            return None
        self.prune_helper(root, nodes)
        return root