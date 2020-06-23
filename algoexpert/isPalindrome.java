package algoexpert;

/**
 * Created by anilgherra on 5/16/20.
 */
public class isPalindrome {
    public static boolean isPalindrome(String str) {

        return checkPalindromRecursively(str, 0, str.length()-1);
    }

    private static boolean checkPalindromRecursively(String str, int left, int right) {
        System.out.println("left: " + left);
        System.out.println("right: " + right);
        if(left >= right) {
            return true;
        }

        char leftCharacter = str.charAt(left);
        char rightCharacter = str.charAt(right);


        if(leftCharacter == rightCharacter) {
            return checkPalindromRecursively(str, left + 1, right - 1);
        } else {
            return false;
        }
    }
    public static void main(String[] args) {
        String str = "kookook";
        System.out.print(isPalindrome(str));
    }
}
