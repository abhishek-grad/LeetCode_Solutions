# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = 0
        children = set()
        adj = defaultdict(list)

        for p, c, il in descriptions:
            children.add(c)
            adj[p].append((c, il))

        for p, c, il in descriptions:
            if not p in children:
                root = p
                break

        res = TreeNode(root)
        q = deque([res])

        while q:
            node = q.popleft()
            for ch, il in adj[node.val]:
                if il: node.left = TreeNode(ch)
                else: node.right = TreeNode(ch)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return res
        