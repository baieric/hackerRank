import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/sherlock-and-anagrams

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numCases = in.nextInt();
        for(int i = 0; i < numCases; i++){
            String str = in.next();
            int anagrams = 0;

            for(int j = 0; j < str.length(); j++){
                for(int k = j+1; k <= str.length(); k++){
                    char[] arr1 = str.substring(j, k).toCharArray();
                    Arrays.sort(arr1);
                    for(int m = j+1; m <= str.length() - (k - j); m++){
                        char[] arr2 = str.substring(m, m + k - j).toCharArray();
                        Arrays.sort(arr2);
                        if(Arrays.equals(arr1, arr2)){
                            anagrams++;
                        }
                    }
                }
            }

            System.out.println(anagrams);
        }
    }
}
