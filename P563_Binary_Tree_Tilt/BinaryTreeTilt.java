/*
* Definition for a binary tree node
* */
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        val = x;
    }
}

public class BinaryTreeTilt {
    private int tilt = 0;

    public int findTilt (TreeNode root) {
        if(root == null) {
            return 0;
        }
        recursion(root);
        return tilt;
    }

    public int recursion (TreeNode root) {
        int leftSum = root.val;
        int rightSum = root.val;
        if (root.left == null && root.right == null) {
            return root.val;
        }
        if (root.left != null) {
            leftSum += recursion(root.left);
        }
        if (root.right != null) {
            rightSum += recursion(root.right);
        }
        tilt += Math.abs(leftSum - rightSum);
        return leftSum + rightSum - root.val;
    }
}

