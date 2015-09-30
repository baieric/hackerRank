import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/bfsshortreach

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int i = 0; i < T; i++){
            int N = in.nextInt();
            int M = in.nextInt();
            int[][] graph = new int[N+1][N+1];
            for(int j = 0; j < M; j++){
                int u = in.nextInt();
                int v = in.nextInt();
                graph[u][v] = 1;
                graph[v][u] = 1;
            }

            int start = in.nextInt();
            boolean[] traversed = new boolean[N+1];
            traversed[start] = true;
            traversed[0] = true;

            int[] distance = new int[N+1];

            LinkedList<Integer> q = new LinkedList<>();
            q.add(start);
            while(q.peek() != null){
                int curr = q.remove();
                for(int j = 1; j <= N; j++){
                    if(traversed[j] == false && graph[curr][j] == 1){
                        traversed[j] = true;
                        distance[j] = distance[curr] + 1;
                        q.add(j);
                    }
                }
            }

            for(int j = 1; j <= N; j++){
                if(distance[j] > 0){
                    System.out.print(distance[j] * 6 + " ");
                }else if(j != start){
                    System.out.print("-1 ");
                }
            }
            System.out.print("\n");
        }
    }
}
