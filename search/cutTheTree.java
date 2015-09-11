import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/cut-the-tree

public class Solution {

    public static class Node {
        public int value;
        public List<Node> neighbours;
        public Node parent;
        public int sum;

        public Node(int val) {
            value = val;
            neighbours = new LinkedList<Node>();
            parent = null;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numNodes = in.nextInt();
        Node[] arr = new Node[numNodes+1];
        int total = 0;
        for(int i = 1; i <= numNodes; i++){
            int val = in.nextInt();
            arr[i] = new Node(val);
            total += val;
        }
        for(int i = 0; i < numNodes - 1; i++){
            int vertex1 = in.nextInt();
            int vertex2 = in.nextInt();
            arr[vertex1].neighbours.add(arr[vertex2]);
            arr[vertex2].neighbours.add(arr[vertex1]);
        }
        setSum(arr[1]);

        int min = Integer.MAX_VALUE;
        for(int i = 1; i <= numNodes; i++){
            for(Node child : arr[i].neighbours){
                int diff = Math.abs(total - child.sum - child.sum);
                if(diff < min){
                    min = diff;
                }
            }
        }
        System.out.println(min);
    }

    public static int setSum(Node parent){
        int sum = parent.value;
        for(Node child : parent.neighbours){
            if(child != parent.parent){
                child.parent = parent;
                sum += setSum(child);
            }
        }
        parent.sum = sum;
        return sum;
    }
}
