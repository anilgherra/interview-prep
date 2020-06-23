package randomPractice;

/**
 * Created by anilgherra on 6/21/20.
 */
public class Search {

    public static void main(String[] args) {
        System.out.println(binarySearch(new int[]{0, 1, 2, 3, 4, 5}, 4, 0, 6));
    }

    public static boolean binarySearch(int[] array, int containsValue, int leftIndex, int rightIndex) {
        int middle = array.length/2;
        if(array[middle] == containsValue) {
            return true;
        } else if(array[middle] > containsValue) {
            rightIndex = middle;
            binarySearch(array, containsValue, 0, rightIndex -1);
        } else if(array[middle] < containsValue) {
            leftIndex = middle;
            binarySearch(array, containsValue,leftIndex + 1  , array.length-1);
        }
        return false;
    }

    public static boolean linearSearch(int[] array, int containsValue) {

        for(int i = 0; i < array.length; i++) {
            if(array[i] == containsValue) {
                return true;
            }
        }
        return false;
    }
}
