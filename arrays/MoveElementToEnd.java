package arrays;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by anilgherra on 6/23/20.
 *
 * Ask: given an array and an integer - move all the occurrences of that element to the end of array.
 */
public class MoveElementToEnd {

    public static void moveElementToEnd(List<Integer> array, int toMove) {
        // Write your code here.
        int start = 0;
        int end = array.size() - 1;

        while(end > start) {
            int startElement = array.get(start);
            int endElement = array.get(end);

            if(startElement == toMove && endElement == toMove) {
                end--;
            } else if( startElement == toMove && endElement != toMove) {
                Collections.swap(array, start, end);
                start++;
                end--;
            } else  {
                start++;
            }
        }
    }

    public static void main(String[] args) {
        List<Integer> integerArray = Arrays.asList(2, 1, 2, 2, 2, 3, 4, 2);
        moveElementToEnd(integerArray, 2);

        for(int element: integerArray){
            System.out.print(element + " ");
        }
    }
}
