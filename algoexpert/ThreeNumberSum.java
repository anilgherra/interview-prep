package algoexpert;

import java.util.*;

/**
 * Created by anilgherra on 5/18/20.
 */
public class ThreeNumberSum {

    public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
        List<Integer[]> tripletArray = new ArrayList<>();

        Arrays.sort(array);
        for(int i = 0; i < array.length; i++) {
            int x = array[i];
            int leftPointer = i + 1;
            int lastPointer = array.length-1;
            while(leftPointer < lastPointer) {
//              System.out.println("LEFT POINTER:  " + leftPointer + " RIGHT POINTER: "+ lastPointer);
                int sum = x + array[leftPointer] + array[lastPointer];
                System.out.println("X: " + x + " Y:" + array[leftPointer] + " Z: " + array[lastPointer] + " SUM: " + sum);
                if(sum == targetSum) {
                    Integer[] tripleValue = {x, array[leftPointer],array[lastPointer]};
                    tripletArray.add(tripleValue);
                    lastPointer--;
                    leftPointer++;
                } else if(sum > targetSum) {
                    lastPointer--;
                } else if(sum < targetSum){
                    leftPointer++;
                }
            }

        }
        return tripletArray;
    }

    public static void printArray(Integer[] array){
        for(Integer element: array) {
            System.out.print(element + "  ");
        }
    }
    public static void main(String[] args){
        int[] unsortedArray = new int[]{12, 3,1,2,-6,5, -8, 6};
        for(Integer[] element : threeNumberSum(unsortedArray, 0)){
            printArray(element);
        }
    }
}
