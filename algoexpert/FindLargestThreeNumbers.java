package algoexpert;

/**
 * Created by anilgherra on 5/15/20.
 */
public class FindLargestThreeNumbers {
    public static int[] findThreeLargestNumbers(int[] array) {

        int[] threeLargest = new int[]{Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE,};
        for(int i = 0; i < array.length; i++) {
            updateLargest(threeLargest, array[i]);
        }
        return threeLargest;
    }

    private static void updateLargest(int[] largestTrackerArray, int digit) {
        if(largestTrackerArray[2] < digit) {
            arrayShifter(largestTrackerArray, 2, digit);
        } else if(largestTrackerArray[1] < digit) {
            arrayShifter(largestTrackerArray, 1, digit);
        } else if(largestTrackerArray[0] < digit) {
            arrayShifter(largestTrackerArray, 0, digit);
        }
    }

    private static void arrayShifter(int[] array, int index, int value) {
            for(int i = 0; i < index; i++) {
                array[i] = array[i+1];
            }
            array[index] = value;
    }

    public static void printArray(int[] array){
        for(Integer element: array) {
            System.out.print(element + " ");
        }
    }

    public static void main(String[] args) {
        int[] array = new int[]{141, 1, 17, -7, 700, 18, 541, 8, 7, 7};
        printArray(findThreeLargestNumbers(array));
    }
}
