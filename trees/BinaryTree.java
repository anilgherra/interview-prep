package trees;

/**
 * Created by anilgherra on 5/22/20.
 */
public class BinaryTree {
    Node root;

    public void addNode(int data) {
       root = addNodeRecursively(root, data);
    }

    private Node  addNodeRecursively(Node currentNode, int data) {
        if(currentNode == null) {
            return new Node(data);
        }

        if(currentNode.left == null) {
            currentNode.left = new Node(data);
        } else {
            currentNode.left = addNodeRecursively(currentNode.left, data);
        }

        if(currentNode.right == null) {
            currentNode.right = new Node(data);
        } else {
            currentNode.right= addNodeRecursively(currentNode.right, data);
        }

        return currentNode;

    }

    /**
     *
     */
    public void printTree() {
         printTreeRecursively(root);
    }

    /**
     *
     * @param currentNode
     */
    private void printTreeRecursively(Node currentNode) {
        System.out.println("Current Node: " + currentNode.data);
        if(currentNode.left != null) {
            printTreeRecursively(currentNode.left);
        }

        if(currentNode.right != null) {
            printTreeRecursively(currentNode.right);
        }
    }

    public void printRoot() {
        System.out.println(root.data);
    }

    class Node {
        Node left, right;
        int data;

        /**
         * Constructor for node.
         * @param data add node
         */
        public Node(int data) {
            this.data = data;
        }
    }

    public static void main(String[] args) {
        BinaryTree binaryTree = new BinaryTree();
        binaryTree.addNode(6);
        binaryTree.addNode(10);

        binaryTree.printTree();

//        binaryTree.printRoot();
    }
}
