public class BalancedTree {
    // A balanced binary tree, also referred to as a height-balanced binary tree, 
    // is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { 
            this.val = val; 
        }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static int Balance(TreeNode root){
        if(root==null)return 0;
        int leftHeight=Balance(root.left);
        if(leftHeight==-1) return -1;
        int rightHeight=Balance(root.right);
        if(rightHeight==-1) return -1;
        if(Math.abs(leftHeight-rightHeight)>1) return -1;
        return Math.max(leftHeight,rightHeight)+1;
    }

    public static boolean isBalanced(TreeNode root) {
        return Balance(root)!=-1;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        if(isBalanced(root)) {
            System.out.print("Tree Is Balanced");
        } else {
            System.out.print("Tree Is not Balanced");
        }
    }

}
