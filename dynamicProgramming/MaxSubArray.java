import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/maxsubarray

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int i = 0; i < T; i++){
            int N = in.nextInt();
            int[] arr = new int[N];
            for(int j = 0; j < N; j++){
                arr[j] = in.nextInt();
            }
            int maxEndingHere = arr[0];
            int max = arr[0];
            int posSum = Math.max(arr[0], 0);
            int maxInt = arr[0];
            for(int j = 1; j < N; j++){
                maxEndingHere = Math.max(maxEndingHere + arr[j], 0);
                max = Math.max(max, maxEndingHere);
                if(maxInt < arr[j]) maxInt = arr[j];
                if(arr[j] > 0) posSum+= arr[j];
            }
            int answer = maxInt > 0 ? posSum : maxInt;
            if(posSum == 0) max = maxInt;
            System.out.println(max + " " + answer);
        }
    }
}
