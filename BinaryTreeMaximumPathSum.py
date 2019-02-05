# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_path(node):
            if node is None:
                return 0, float('-inf')
            to_left, in_left = max_path(node.left)
            to_right, in_right = max_path(node.right)
            to_node = node.val + max(0, to_left, to_right)
            in_node = max(in_left, in_right, to_left + node.val + to_right, to_node)
            return to_node, in_node
        return max_path(root)[1]