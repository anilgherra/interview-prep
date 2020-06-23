package algoexpert;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by anilgherra on 5/16/20.
 */
public class ValidateSubsequence {
    public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence) {
        // Write your code here.
        int sequenceIndex = 0;
        for(int i = 0; i < array.size(); i++) {
        if(array.get(i).equals(sequence.get(sequenceIndex))) {
            sequenceIndex++;
            if(sequenceIndex == sequence.size()) {
                return true;
            }
        }
    }
    return sequenceIndex == sequence.size();
}

    public static void main(String[] args) {
        List<Integer> array = Arrays.asList(5,1, 22, 25, 6, -1, 8, 10);
        List<Integer> subSequence = Arrays.asList(22, 25, 6);
        System.out.print(isValidSubsequence(array, subSequence));
    }
}
