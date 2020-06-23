package algoexpert;

import java.util.Arrays;

/**
 * Created by anilgherra on 5/21/20.
 */
public class MonotonicArray {

    public static boolean isMonotonic(int[] array) {
        // Write your code here.
        boolean flag = false;
        boolean decreasingOrder = true;
        boolean increasingOrder = true;
        if(array.length == 0 ) {
            return flag;
        }
        for(int i = 0; i < array.length-1; i++) {

        }

        return flag;
    }

    

    public static void main(String[] args) {
        int[] array = {-1, -5, -10, -1100, -1100, 100000, -1102, -9001};
        System.out.println(isMonotonic(array));
    }
}
