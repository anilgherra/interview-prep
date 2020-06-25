package arrays;

/**
 * Created by anilgherra on 6/24/20.
 * Problem: Create method that takes positive integers and
 * returns the maximum sum of non-adjacent elements in array.
 */
public class MaximumSumOfNonAdjacentSubset {

    public static int maxSubsetSumNoAdjacent(int[] array) {
        if(array.length == 0) {
            return 0;
        }

        if(array.length == 1) {
            return array[0];
        }

        int[] maxSumArray = new int[array.length];

        //bases cases
        maxSumArray[0] = array[0];
        maxSumArray[1] = Math.max(array[0], array[1]);

        //using pre-calculated computation to determine max sum for next iteration.
        for(int i = 2; i < array.length; i++) {
            maxSumArray[i] = Math.max(maxSumArray[i-1], maxSumArray[i-2] + array[i]);
        }
        return maxSumArray[maxSumArray.length-1];
    }

    public static void main(String[] args) {
        System.out.println(maxSubsetSumNoAdjacent(new int[]{75, 105,120,75,90,135}));
    }
}
