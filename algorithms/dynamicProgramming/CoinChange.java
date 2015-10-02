import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/coin-change

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();
        int[] val = new int[M];
        for(int i = 0; i < M; i++){
            val[i] = in.nextInt();
        }

        long[] arr = new long[N+1];
        arr[0] = 1;
        for(int i = 0; i < M; i++){
            for(int j = val[i]; j <= N; j++){
                arr[j] += arr[j - val[i]];
            }
        }
        System.out.println(arr[N]);
    }
}
