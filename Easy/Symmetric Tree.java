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
    public boolean isSymmetric(TreeNode root) {
        
        ArrayList<Integer> res = new ArrayList<>();
        if(root.left != null)
            res = recurLeft(root.left,res);
        //int last = res.size() - 1;
        //res.remove(last);
        ArrayList<Integer> rev = new ArrayList<>();
        if(root.right != null)
            rev = recurRight(root.right,rev);
        //Collections.reverse(rev);
        //System.out.println(res);
        //System.out.println(rev);
        return res.equals(rev);
    }
    
    public ArrayList<Integer> recurLeft(TreeNode root, ArrayList<Integer> res) {
        
        if (root.left != null)
            recurLeft(root.left,res);
        else
            res.add(null);
            
        if (root.right != null)
            recurLeft(root.right,res);
        else
            res.add(null);
        
        res.add(root.val); //3 4 2 2 4 3 1
            
        return res;
    }
    
    public ArrayList<Integer> recurRight(TreeNode root, ArrayList<Integer> res) {
        
        if (root.right != null)
            recurRight(root.right,res);
        else
            res.add(null);
        
        if (root.left != null)
            recurRight(root.left,res);
        else
            res.add(null);
        
        res.add(root.val); //3 4 2 2 4 3 1
            
        return res;
    }
}
