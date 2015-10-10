import java.io.*;
import java.util.*;

// Solution to https://www.hackerrank.com/challenges/journey-to-the-moon

public class Solution {
    public static Node[] graph;
    public static boolean[] traversed;
    public static int N;

    public static int getNum(int v){
        if(graph[v] == null) return 1;
        traversed[v] = true;
        int count = 1;
        for(Node n : graph[v].neighbours){
            if(!traversed[n.index]) count += getNum(n.index);
        }
        return count;
    }

    public static class Node{
        public ArrayList<Node> neighbours;
        public int index;
        public Node(int i){
            index = i;
            neighbours = new ArrayList<>();
        }
    }

   public static void main(String[] args) throws Exception{
        BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = bfr.readLine().split(" ");
        N = Integer.parseInt(temp[0]);
        int I = Integer.parseInt(temp[1]);

       graph = new Node[N];
       traversed = new boolean[N];

        for(int i = 0; i < I; i++){
            temp = bfr.readLine().split(" ");
            int a = Integer.parseInt(temp[0]);
            int b = Integer.parseInt(temp[1]);
            if(graph[a] == null){
                graph[a] = new Node(a);
            }
            if(graph[b] == null){
                graph[b] = new Node(b);
            }
            graph[a].neighbours.add(graph[b]);
            graph[b].neighbours.add(graph[a]);
        }

       ArrayList<Integer> arr = new ArrayList<>();
       int ones = 0;
       for(int i = 0; i < N; i++){
           if(!traversed[i]){
               int num = getNum(i);
               if(num == 1) ones++;
               else arr.add(num);
           }
       }

       long combinations = 0;

       for(int i = 0; i < arr.size(); i++){
           for(int j = i+1; j < arr.size(); j++){
               combinations += arr.get(i) * arr.get(j);
           }
           combinations += arr.get(i) * ones;
       }
       long choosetwo = (long) ones * (ones - 1) / 2;
       combinations += choosetwo;

        System.out.println(combinations);

    }
}
