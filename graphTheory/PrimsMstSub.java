import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/primsmstsub

public class Solution {

    public static int minKeyNotTraversed(int numNodes, int[] key, boolean[] traversed){
        int min = Integer.MAX_VALUE;
        int min_index = 0;

       for (int i = 1; i <= numNodes; i++){
         if (traversed[i] == false && key[i] < min){
             min = key[i];
             min_index = i;
         }
       }
       return min_index;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numNodes = in.nextInt();
        int numEdges = in.nextInt();
        int[][] graph = new int[numNodes + 1][numNodes+1];
        for(int i = 1; i <= numNodes; i++){
            for(int j = 1; j <= numNodes; j++){
                graph[i][j] = Integer.MAX_VALUE;
            }
        }

        int[] key = new int[numNodes + 1];
        boolean[] traversed = new boolean[numNodes + 1];
        for(int i = 0; i < numEdges; i++){
            int node1 = in.nextInt();
            int node2 = in.nextInt();
            int length = in.nextInt();
            if(length < graph[node1][node2]){
                graph[node1][node2] = length;
                graph[node2][node1] = length;
            }
        }

        for(int i = 1; i <= numNodes; i++){
            traversed[i] = false;
            key[i] = Integer.MAX_VALUE;
        }
        // index 0 is not used, just say it's traversed
        traversed[0] = true;

        int start = in.nextInt();
        key[start] = 0;

        int length = 0;

        for(int i = 1; i <= numNodes; i++){
            int nextNode = minKeyNotTraversed(numNodes, key, traversed);
            traversed[nextNode] = true;
            length += key[nextNode];
            for(int j = 1; j <= numNodes; j++){
                if(traversed[j] == false && graph[nextNode][j] < key[j]){
                    key[j] = graph[nextNode][j];
                }
            }
        }
        System.out.println(length);
    }
}
