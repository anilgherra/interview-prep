package trees;

/**
 * Created by anilgherra on 5/16/20.
 */
public class BinarySearchTree {
    Node root;

    public void insert(int value) {
        // Write your code here.
        root = insertRecursively(root, value);
        // Do not edit the return statement of this method.

    }

    private Node insertRecursively(Node currentNode, int value) {
        if (currentNode == null) {
            return new Node(value);
        }

        if (currentNode.data >= value) {
            if (currentNode.left == null) {
                currentNode.left = new Node(value);
            } else {
                currentNode.left = insertRecursively(currentNode.left, value);
            }
        } else {
            if (currentNode.right == null) {
                currentNode.right = new Node(value);
            } else {
                currentNode.right = insertRecursively(currentNode.right, value);
            }
        }

        return currentNode;
    }

    public boolean contains(int value) {
        return checkContainsRecursively(root, value);
    }

    private boolean checkContainsRecursively(Node currentNode, int data) {
        boolean isContained = false;
        if (currentNode == null) {
            return isContained;
        }

        if (currentNode.data == data) {
            return true;
        } else if (currentNode.data > data) {
            return (currentNode.left != null && checkContainsRecursively(currentNode.left, data));
        } else if (currentNode.data < data) {
            return currentNode.right != null && checkContainsRecursively(currentNode.right, data);
        }
        return isContained;
    }

    private void printTreeRecursively(Node currentNode) {
        System.out.println(currentNode.data);

        if (currentNode.left != null) {
            printTreeRecursively(currentNode.left);
        }

        if (currentNode.right != null) {
            printTreeRecursively(currentNode.right);
        }
    }

    public void printTree() {
        printTreeRecursively(root);
    }

    public void remove(int value) {
        removeRecursively(root, value);
    }

    private void removeRecursively(Node currentNode, int data) {
        if (currentNode.data == data) {
            System.out.println("Found node with data: " + data);

            if (currentNode.left == null && currentNode.right == null) {
                System.out.println("I'm a leaf node: " + data);
                currentNode = null;
                return;
            }
        }

        if (currentNode.data > data) {
            if (currentNode.left != null) {
                removeRecursively(currentNode.left, data);
            }
        } else {
            if (currentNode.right != null) {
                removeRecursively(currentNode.right, data);
            }
        }
    }


    class Node {
        int data;
        Node left, right;

        public Node(int data) {
            this.data = data;
        }

    }

    public static void main(String[] args) {
        BinarySearchTree binarySearchTree = new BinarySearchTree();

        binarySearchTree.insert(20);
        binarySearchTree.insert(15);
        binarySearchTree.insert(10);
        binarySearchTree.insert(18);
        binarySearchTree.insert(25);
        binarySearchTree.insert(23);
        binarySearchTree.insert(30);


        binarySearchTree.remove(30);
        binarySearchTree.printTree();
//        System.out.println(binarySearchTree.contains(30));
    }
}
