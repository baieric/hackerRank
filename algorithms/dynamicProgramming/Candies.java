import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/candies

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++){
            arr[i] = in.nextInt();
        }
        int candies = 1;
        int rating = arr[0];
        int total = 1;

        int peakIndex = 0;
        int peakCandies = 1;

        for(int i = 1; i < N; i++){
            if(arr[i] == rating){
                candies = 1;
                peakIndex = i;
                peakCandies = candies;
            }else if(arr[i] > rating){
                candies++;
                peakIndex = i;
                peakCandies = candies;
            }else{
                candies = 1;
                total+= i - peakIndex - 1;
                if(i - peakIndex >= peakCandies){
                    total++;
                }
            }
            rating = arr[i];
            total += candies;
        }
        System.out.println(total);
    }
}
