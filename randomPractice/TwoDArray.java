package randomPractice;

/**
 * Created by anilgherra on 5/18/20.
 */
public class TwoDArray {

    public static void main(String[] args) {
        int[][] twoDArray = new int[5][];

        for(int i = 0; i < twoDArray.length; i++){
//            for(int j  = 0; j < twoDArray[0].length; j++){
//                twoDArray[i][j] = increment;
//                increment++;
//            }
            twoDArray[i] = new int[i+1];
        }

        int increment = 1;
        for(int i = 0; i < twoDArray.length; i++){
            for(int j  = 0; j < twoDArray[i].length; j++){
                twoDArray[i][j] = increment;
                increment++;
            }
        }


        for(int i = 0; i < twoDArray.length; i++){
            for(int j  = 0; j < twoDArray[i].length; j++){
                System.out.print(twoDArray[i][j] + "  ");
            }
            System.out.println();
        }
    }

}
