package algoexpert;

import java.util.Arrays;
import java.util.List;

/**
 * Created by anilgherra on 5/21/20.
 */

//TODO: finish this problem correctly
public class MoveElementToEnd {

    public static List<Integer> moveElementToEnd(List<Integer> array, int toMove) {

        // Write your code here.
        for(int i = 0 ; i < array.size()-1; i++) {

            if(array.get(i) == toMove) {
                int nextElement = array.get(i+1);
                array.add(array.size()-1, array.get(i));
                array.add(i, nextElement);
            }
        }
        return array;
    }

    public static void printArray(List<Integer> array){
        for(Integer element: array) {
            System.out.print(element + "  ");
        }
    }

    public static void main(String[] args) {
        List<Integer> array = Arrays.asList(2, 1, 2, 2, 2, 3, 4, 2);
        printArray(moveElementToEnd(array, 2));
    }
}
