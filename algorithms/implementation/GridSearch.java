import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/the-grid-search

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int numCases = in.nextInt();
        for(int i = 0; i < numCases; i++){
            int gridRows = in.nextInt();
            int gridCols = in.nextInt();
            String[] grid = new String[gridRows];
            for(int j = 0; j < gridRows; j++){
                grid[j] = in.next();
            }

            int pattRows = in.nextInt();
            int pattCols = in.nextInt();
            String[] patt = new String[pattRows];
            for(int j = 0; j < pattRows; j++){
                patt[j] = in.next();
            }

            String answer = "NO";
            for(int j = 0; j < gridRows - pattRows + 1; j++){
                boolean mismatch = false;
                int gridIndex = grid[j].indexOf(patt[0]);
                if(gridIndex >= 0){
                    for(int k = 1; k < pattRows; k++){
                        String str = grid[j+k].substring(gridIndex, gridIndex + pattCols);
                        if (!str.equals(patt[k])){
                            mismatch = true;
                            break;
                        }
                    }
                } else{
                    mismatch = true;
                }

                if(!mismatch){
                    answer = "YES";
                    break;
                }
            }
            System.out.println(answer);
        }

    }
}
