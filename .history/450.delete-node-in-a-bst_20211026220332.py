#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    #     if not root:
    #         return root

    #     prev, curr=TreeNode(-1),root
    #     while curr:
    #         if key<curr.val:
    #             prev=curr
    #             curr=curr.left
    #         if key>curr.val:
    #             prev=curr
    #             curr=curr.right

    #         if curr.val==key:
    #             if curr.left and curr.right:
    #                 if curr.val>prev.val:
    #                     prev.right=curr.left
    #                     curr.left.right=curr.right
    #             elif curr.left and not curr.right:
    #                 if curr.val>prev.val:
    #                     prev.right=curr.left
    #                 else:
    #                     prev.left=curr.left
    #             elif not curr.left and curr.right:
    #                 if curr.val>prev.val:
    #                     prev.right=curr.right
    #                 else:
    #                     prev.left=curr.right
    #             else:
    #                 if curr.val>prev.val:
    #                     prev.right=None
    #                 else:
    #                     prev.left=None
    #         return root
            


    def deleteNode(root, key):
        if not root: # if root doesn't exist, just return it
            return root
        if root.val > key: # if key value is less than root value, find the node in the left subtree
            root.left = deleteNode(root.left, key)
        elif root.val < key: # if key value is greater than root value, find the node in right subtree
            root.right= deleteNode(root.right, key)
        else: #if we found the node (root.value == key), start to delete it
            if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
                return root.left
            if not root.left: # if it has no left children, we delete the node then new root would be root.right
                return root.right
                # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini # replace value
            root.right = deleteNode(root.right,root.val) # delete the minimum node in right subtree
        return root

# @lc code=end

