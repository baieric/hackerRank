import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/palindrome-index

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int i = 0; i < T; i++){
            String s = in.next();
            int l = 0;
            int r = s.length() - 1;
            int index = -1;
            while(l < r){
                if(s.charAt(l) != s.charAt(r)){
                    String left = s.substring(l, r);
                    String right = s.substring(l+1, r+1);
                    if(left.equals(new StringBuilder(left).reverse().toString())){
                        index = r;
                        break;
                    }else if(right.equals(new StringBuilder(right).reverse().toString())){
                       index = l;
                       break;
                    } else{
                        index = -1;
                        break;
                    }
                }else{
                    l++;
                    r--;
                }
            }
            System.out.println(index);
        }
    }
}
