/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        
        if (root == null)
            return 0;
       
        return recurDepth(root, 1);
    }
    public int recurDepth(TreeNode root, int depth){
        int l=0,r=0;
        
        if (root.left == null && root.right == null)
            return depth;
        if(root.left != null){
            l=recurDepth(root.left, depth+1);
        }
        if(root.right != null){
            r=recurDepth(root.right, depth+1);
        }
        
        depth = l>r?l:r;
        return depth;
        
    }
}
