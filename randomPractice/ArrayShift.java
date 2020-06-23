package randomPractice;

/**
 * Created by anilgherra on 5/14/20.
 */
public class ArrayShift {

    public static void main(String[] args) {
        int[] array = new int[4];
        array[0] = 1;
        array[1] = 2;
        array[2] = 3;
        array[3] = 4;
        arrayShifter(array, 1, "left");
        arrayShifter(array, 1, "right");
        printArray(array);
    }

    public static void printArray(int[] array){
        for(Integer element: array) {
            System.out.print(element + " ");
        }
    }

    public static int[] arrayShifter(int[] arrayToShift, int shiftBy, String shiftOption) {
        if(shiftOption.equals("left")) {
            for(int s = 0; s < shiftBy; s++) {
                for (int i = 0; i < arrayToShift.length - 1; i++) {
                    arrayToShift[i] = arrayToShift[i + 1];
                    if (i == arrayToShift.length - 2) {
                        arrayToShift[i + 1] = 0;
                    }
                }
            }
            return arrayToShift;
        }

        if(shiftOption.equals("right")) {
            for(int s = 0; s < shiftBy; s++) {
                for (int i =  arrayToShift.length -1 ; i > 0 ; i--) {
                    arrayToShift[i] = arrayToShift[i - 1];
                    if(i == 1) {
                        arrayToShift[i-1] = 0;
                    }
                }
            }
            return arrayToShift;
        }

        return arrayToShift;
    }

}
