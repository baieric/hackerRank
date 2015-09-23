import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/stockmax
// Dynamic programming not required for this question... Can be solved linearly without DP

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();

        for(int i = 0; i < T; i++){
            int N = in.nextInt();
            int[] prices = new int[N];
            for(int j = 0; j < N; j++){
                int price = in.nextInt();
                prices[j] = price;
            }
            int max = 0;
            long profit = 0;
            for(int j = N - 1; j >= 0; j--){
                if(prices[j] > max){
                    max = prices[j];
                }else{
                    profit+= max - prices[j];
                }
            }
            System.out.println(profit);
        }
    }
}
