import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/missing-numbers

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int sizeA = in.nextInt();
        HashMap<Integer, Integer> hashA = new HashMap<Integer, Integer>();
        for(int i = 0; i < sizeA; i++){
            int num = in.nextInt();
            if(hashA.containsKey(num)){
                int val = hashA.get(num);
                hashA.put(num, val+1);
            }else{
                hashA.put(num, 1);
            }
        }
        int sizeB = in.nextInt();
        int[] arr = null;
        for(int i = 0; i < sizeB; i++){
            int num = in.nextInt();
            int val = hashA.get(num);
            if(val > 0){
                hashA.put(num, val - 1);
            }else{
                if(arr == null){
                    arr = new int[num + 100];
                }
                arr[num]++;
            }
        }

        for(int i = 0; i < arr.length; i++){
            if(arr[i] > 0){
                System.out.print(i + " ");
            }
        }
    }
}
