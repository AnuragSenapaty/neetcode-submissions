# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fullTraversal(root:Optional(TreeNode), depth:int) -> int:
            if not root:
                return depth
            else:
                return max(fullTraversal(root.right, depth+1), fullTraversal(root.left, depth+1))
        return fullTraversal(root, 0)


        