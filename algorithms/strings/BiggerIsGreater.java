import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/bigger-is-greater

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numCases = in.nextInt();
        for(int i = 0; i < numCases; i++){
            String str = in.next();
            int lastBadIndex = -1;
            for(int j = str.length() - 1; j > 0; j--){
                if(str.charAt(j) > str.charAt(j-1)){
                    lastBadIndex = j -1;
                    break;
                }
            }
            if(lastBadIndex == -1){
                System.out.println("no answer");
            }else{
                char ch = str.charAt(lastBadIndex);
                char minAboveCh = 'z' + 1;
                int index = -1;
                for(int j = lastBadIndex; j < str.length(); j++){
                    char candidate = str.charAt(j);
                    if(candidate > ch && candidate < minAboveCh){
                        minAboveCh = candidate;
                        index = j;
                    }
                }
                char[] array = str.substring(lastBadIndex + 1).toCharArray();
                array[index - lastBadIndex - 1] = ch;
                Arrays.sort(array);
                String newStr = new String(array);
                String answer = str.substring(0, lastBadIndex) + minAboveCh + newStr;
                System.out.println(answer);
            }
        }
    }
}
