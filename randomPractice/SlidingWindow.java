package randomPractice;

/**
 * Created by anilgherra on 5/20/20.
 */
public class SlidingWindow {

//    public static void traverseWithFixedWindow(int[] array, int sizeK) {
//        for(int i = 0; i <= array.length-sizeK; i++) {
//            int left = i;
//            int right = i + sizeK;
//            for(int j = left; j < right; j++) {
//                System.out.print(array[j] + " ");
//            }
//            System.out.println();
//        }
//    }

    public static int findMinimumSumBetweenThreeElements(int[] array, int sizeK) {
        int minStarter = Integer.MAX_VALUE;


        for(int i = 0; i <= array.length-sizeK; i++) {
            int left = i;
            int right = i + sizeK;
            int windowSum = 0;
            for(int j = left; j < right; j++) {
               windowSum +=  array[j];
            }
            minStarter = Math.min(minStarter, windowSum);
            System.out.println("New lowest sum: " + windowSum);
        }
        return minStarter;
    }

    public static void main(String[] args) {
        int[] array = {1,3,5,5,-50, 200};

//            traverseWithFixedWindow(array, 3);
            System.out.println(findMinimumSumBetweenThreeElements(array, 3));
    }

}
