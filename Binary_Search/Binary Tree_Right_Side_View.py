from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node, depth, result):
        if not node:
            return

        # If this depth is visited first time, add node value
        if depth == len(result):
            result.append(node.val)

        # Visit right first, then left
        self.dfs(node.right, depth + 1, result)
        self.dfs(node.left, depth + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, 0, result)
        return result


# -----------------------
# Function call / Testing
# -----------------------

# Create a sample tree:
#        1
#       / \
#      2   3
#       \   \
#        5   4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

# Call the function
sol = Solution()
output = sol.rightSideView(root)

print("Right Side View:", output)

# Time complexity: O(log n)
# Space complexity: O(n)
