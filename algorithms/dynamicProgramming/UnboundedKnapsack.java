import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/unbounded-knapsack

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int i = 0; i < T; i++){
            int N = in.nextInt();
            int K = in.nextInt();
            int[] arr = new int[N];
            for(int j = 0; j < N; j++){
                arr[j] = in.nextInt();
            }

            boolean[] ans = new boolean[K+1];
            ans[0] = true;
            int max = 0;
            for(int j = 1; j <= K; j++){
                for(int k = 0; k < N; k++){
                    if(j-arr[k] >= 0 && ans[j-arr[k]]){
                        ans[j] = true;
                        max = j;
                        break;
                    }
                }
            }
            System.out.println(max);
        }
    }
}
