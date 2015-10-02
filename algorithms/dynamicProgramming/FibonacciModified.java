import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/fibonacci-modified

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        int B = in.nextInt();
        int N = in.nextInt();
        BigInteger[] arr = new BigInteger[N];
        arr[0] = BigInteger.valueOf(A);
        arr[1] = BigInteger.valueOf(B);
        for(int i = 2; i < N; i++){
            arr[i] = arr[i-2].add(arr[i-1].multiply(arr[i-1]));
        }
        System.out.println(arr[N-1]);
    }
}
