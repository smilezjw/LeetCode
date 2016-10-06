package Leetcode;

/**
 * Created by Jiawen on 16/10/6.
 */


/**
 * Definition for a binary tree node.
 **/
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class SumofLeftLeaves{

    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root, false);
    }

    public int dfs(TreeNode root, Boolean isLeft){
        if(root == null){
            return 0;
        }
        if(root.left == null && root.right == null && isLeft){
            return root.val;
        }
        return dfs(root.left, true) + dfs(root.right, false);
    }

    public static void main(String[] args){
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        TreeNode p = root.right;
        p.left = new TreeNode(15);
        p.right = new TreeNode(7);
        p = root.left;
        p.left = new TreeNode(2);

        SumofLeftLeaves solution = new SumofLeftLeaves();
        System.out.println(solution.sumOfLeftLeaves(root));
    }
}

