package algoexpert;

import java.util.HashMap;

/**
 * Created by anilgherra on 5/16/20.
 */
public class CaesarCypherEncryptor {
    public static String caesarCypherEncryptor(String str, int key) {

        String alphabet = "abcdefghijklmnopqrstuvwxyz";


        HashMap<Integer, Character> asciiMapper = new HashMap<>();
        char[] shiftedCharactersArray = new char[str.length()];

        for(int i = 0; i < alphabet.length(); i++) {
            asciiMapper.put((int) alphabet.charAt(i), alphabet.charAt(i));
        }


        key = key % 26;
        for(int j = 0 ; j < str.length(); j++) {
            int lookUpKey = str.charAt(j) + key;
            if(lookUpKey > 122) {
                lookUpKey  = (96 + lookUpKey) % 122  ;
                System.out.print(lookUpKey);
            }
          char shiftedValueLookedUp = asciiMapper.get(lookUpKey);
          shiftedCharactersArray[j] = shiftedValueLookedUp;
        }


        return  String.valueOf(shiftedCharactersArray);

    }

    public static void main(String[] args) {
        String test1 = "abc";
        System.out.println(caesarCypherEncryptor(test1, 56));
    }
}
