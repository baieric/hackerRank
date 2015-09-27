import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/sherlock-and-watson

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner (System.in);
        int N = in.nextInt();
        int K = in.nextInt();
        int Q = in.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++){
            arr[i] = in.nextInt();
        }

        int shift = K % N;
        int[] result = new int[N];
        for(int i = 0; i < N; i++){
            result[(i + shift) % N] = arr[i];
        }

        for(int i = 0; i < Q; i++){
            int idx = in.nextInt();
            System.out.println(result[idx]);
        }
    }
}
