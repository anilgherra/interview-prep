package algoexpert;

import java.util.HashMap;

/**
 * Created by anilgherra on 5/16/20.
 *
 * x + y = z
 */
public class TwoNumberSum {
    public static int[] twoNumberSum(int[] array, int targetSum) {
        HashMap<Integer, Boolean> numbers = new HashMap<>();
        for(int x: array) {
            int neededToCompleteSum = targetSum - x;

            if(numbers.containsKey(neededToCompleteSum)) {
                int[] numbersAddingToSum = new int[2];
                numbersAddingToSum[0] = x;
                numbersAddingToSum[1] = neededToCompleteSum;

               return numbersAddingToSum;
            } else {
                numbers.put(x, true);
            }
        }

        return new int[0];
    }

    public static void printArray(int[] array){
        for(Integer element: array) {
            System.out.print(element + " ");
        }
    }

    public static void main(String[] args) {
        int[] array = new int[]{3, 5, -4, 8, 11, 1, -1, 6};
        int target = 10;

        int[] targetSumArray = twoNumberSum(array, target);
        printArray(targetSumArray);
    }

}
