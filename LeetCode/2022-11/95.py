# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def search(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left_trees = search(start, i-1)
                right_trees = search(i+1, end)
                for left in left_trees:
                    for right in right_trees:
                        curr_node = TreeNode(val=i)
                        curr_node.left = left
                        curr_node.right = right
                        res.append(curr_node)
            return res
        return search(1, n)