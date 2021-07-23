# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getPathToNode(self, root, node):
        path_to_node = []
        cur_node = root
        while True:
            if cur_node.val == node.val:
                path_to_node.append(cur_node)
                break
            elif cur_node.val > node.val:
                path_to_node.append(cur_node)
                cur_node = cur_node.left
            else:
                path_to_node.append(cur_node)
                cur_node = cur_node.right
        return path_to_node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pp = self.getPathToNode(root, p)
        pq = self.getPathToNode(root, q)
        last_success = None
        for i in range(min(len(pp), len(pq))):
            if pp[i].val == pq[i].val:
                last_success = pp[i]
            else:
                break
        return last_success