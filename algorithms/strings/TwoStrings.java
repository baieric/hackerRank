import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/two-strings

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int i = 0; i < T; i++){
            String s1 = in.next();
            String s2 = in.next();
            String ans = "NO";
            for(char c : "abcdefghijklmnopqrstuvwxyz".toCharArray()){
                if(s1.indexOf(c) > -1 && s2.indexOf(c) > -1){
                    ans = "YES";
                    break;
                }
            }
            System.out.println(ans);
        }
    }
}
