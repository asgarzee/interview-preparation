def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if nums:
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
    return None