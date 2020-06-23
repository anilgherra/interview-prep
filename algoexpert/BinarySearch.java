package algoexpert;

import java.util.Arrays;

/**
 * Created by anilgherra on 5/15/20.
 * 1. Data must be first sorted for this to work.
 * 2. Can do it iteratively or recursively.
 */
public class BinarySearch {

    public static boolean binarySearch(int[] array, int value) {
        return binarySearchRecursively(array,value, 0, array.length - 1, 1);
    }

    private static boolean binarySearchRecursively(int[] array, int value, int left, int right, int steps) {
        if(left > right) {
            return  false;
        }
        System.out.println("In step: " + steps);

        int middleIndex =  (left + right) / 2;

        if(array[middleIndex] == value) {
            return true;
        } else if(value < array[middleIndex]) {
            return binarySearchRecursively(array, value, left, middleIndex - 1, steps + 1);
        } else {
            return binarySearchRecursively(array, value, middleIndex + 1, right, steps + 1);
        }
    }

    public static void main(String[] args) {
        int[] array = new int[]{141, 1, 17, -7, 700, 18, 541, 8, 7, 7};
        Arrays.sort(array);
        System.out.print(binarySearch(array, -7));

    }
}
