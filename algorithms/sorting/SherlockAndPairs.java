import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/sherlock-and-pairs/

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

            BigInteger one = BigInteger.valueOf(1);
            HashMap<Integer, BigInteger> count = new HashMap<>();
            for(int j = 0; j < N; j++){
                if(count.containsKey(arr[j])){
                    count.put(arr[j], count.get(arr[j]).add(one));
                }else{
                    count.put(arr[j], one);
                }
            }

            BigInteger num = BigInteger.valueOf(0);
            for(BigInteger value : count.values()){
                if(value.compareTo(one) == 1){
                    BigInteger pairs = value.multiply(value.subtract(one));
                    num = num.add(pairs);
                }
            }
            System.out.println(num);
        }
    }
}
