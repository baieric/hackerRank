import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/kruskalmstrsub

public class Solution {

    public static int N;
    public static int M;
    public static int[][] graph;
    public static boolean[] traversed;

    public static int getMinWeight(){
        int min = Integer.MAX_VALUE;
        int minIndexI = 0; // already traversed node
        int minIndexJ = 0; // node to be added
        for(int i = 1; i <= N; i++){
            if(traversed[i]){
                for(int j = 1; j <= N; j++){
                    if(graph[i][j] != -1 && !traversed[j]){
                        if(graph[i][j] < min){
                            min = graph[i][j];
                            minIndexI = i;
                            minIndexJ = j;
                        } else if(graph[i][j] == min){
                            int weight1 = i + j;
                            int weight2 = minIndexI + minIndexJ;
                            if(weight1 < weight2){
                                minIndexI = i;
                                minIndexJ = j;
                            }
                        }
                    }
                }
            }
        }
        traversed[minIndexJ] = true;
        return min;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        M = in.nextInt();
        graph = new int[N+1][N+1]; //index 0 is never used

        for(int i = 0; i < N+1; i++){
            for(int j = 0; j < N+1; j++){
                graph[i][j] = -1;
            }
        }

        for(int i = 0; i < M; i++){
            int x = in.nextInt();
            int y = in.nextInt();
            int r = in.nextInt();
            if(graph[x][y] == -1 || r < graph[x][y]){
                graph[x][y] = r;
                graph[y][x] = r;
            }
        }

        traversed = new boolean[N+1];
        for(int i = 1; i <= N; i++){
            traversed[i] = false;
        }
        int S = in.nextInt();
        traversed[S] = true;
        int total = 0;
        for(int i = 1; i < N; i++){
            int weight = getMinWeight();
            total += weight;
        }
        System.out.println(total);
    }
}
