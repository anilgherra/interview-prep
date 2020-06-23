package algoexpert;

import java.util.Arrays;

/**
 * Created by anilgherra on 5/21/20.
 */
public class SmallestDifference {

    public static int[] smallestDifference(int[] arrayOne, int[] arrayTwo) {
        // Write your code here.
        Arrays.sort(arrayOne);
        Arrays.sort(arrayTwo);
        int firstPtr = 0;
        int secondPtr = 0;
        int[] smallestDifference = new int[]{Integer.MAX_VALUE, 0};
        while(firstPtr != arrayOne.length && secondPtr != arrayTwo.length){
            if(Math.abs(arrayOne[firstPtr] - arrayTwo[secondPtr]) == 0) {
                return new int[]{arrayOne[firstPtr], arrayTwo[secondPtr]};
            } else {
                if(Math.abs(smallestDifference[0] - smallestDifference[1]) > Math.abs(arrayOne[firstPtr] - arrayTwo[secondPtr] )) {
                    smallestDifference[0] = arrayOne[firstPtr];
                    smallestDifference[1] = arrayTwo[secondPtr];
                }

                int smallerNumber = Math.min(arrayOne[firstPtr], arrayTwo[secondPtr]);
                if(smallerNumber == arrayTwo[secondPtr]) {
                    secondPtr++;
                } else {
                    firstPtr++;
                }
            }

        }
        return smallestDifference;
    }

    public static void printArray(int[] array){
        for(int element: array) {
            System.out.print(element + "  ");
        }
    }

    public static void main(String[] args) {
        int[] array1 = {-1, 5, 10, 20, 28, 3};
        int[] array2 = {26,134,135, 15,17};

        printArray(smallestDifference(array1, array2));

    }
}
