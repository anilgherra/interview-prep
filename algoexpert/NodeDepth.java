package algoexpert;

/**
 * Created by anilgherra on 5/18/20.
 */
public class NodeDepth {
    public static int nodeDepths(BinaryTree root) {
        // Write your code here.
        return getNodeDepthRecursively(root, 0, 0);
    }

    private static int getNodeDepthRecursively(BinaryTree currentNode, int hops, int globalSum) {

        if(currentNode.left != null) {
            hops++;

            getNodeDepthRecursively(currentNode.left, hops, globalSum);
        }

        if(currentNode.right != null) {
            hops++;
            getNodeDepthRecursively(currentNode.right, hops, globalSum);
        }

        return globalSum;
    }


    static class BinaryTree {
        int value;
        BinaryTree left;
        BinaryTree right;

        public BinaryTree(int value) {
            this.value = value;
            left = null;
            right = null;
        }
    }
}
