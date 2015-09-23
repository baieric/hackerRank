import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/quicksort3

public class Solution {

    public static int partition(int[] arr, int l, int r){
        int pivot = arr[r];
        int swapIndex = l;
        for(int i = l; i < r; i++){
            if(arr[i] <= pivot){
                int temp = arr[i];
                arr[i] = arr[swapIndex];
                arr[swapIndex] = temp;
                swapIndex++;
            }
        }
        arr[r] = arr[swapIndex];
        arr[swapIndex] = pivot;

        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.print("\n");

        return swapIndex;
    }

    public static void sort(int[] arr, int low, int high){
        if(low < high){
            int index = partition(arr, low, high);
            sort(arr, low, index - 1);
            sort(arr, index+1, high);
        }

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int[] arr = new int[num];
        for(int i = 0; i < num; i++){
            arr[i] = in.nextInt();
        }
        sort(arr, 0, arr.length - 1);
    }
}
