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
    public List<Integer> inorderTraversal(TreeNode root) {
        
        //System.out.println(root);
        List<Integer> res = new ArrayList<>();
        recurFunc(root,res);
        
        return res;
    }
    //=========
    void recurFunc(TreeNode root, List<Integer> res){
        if (root != null){
            recurFunc(root.left,res);
            res.add(root.val);
            recurFunc(root.right,res);
        }
    }
    //=========
}
