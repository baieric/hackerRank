import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// Solution to https://www.hackerrank.com/challenges/angry-children

// The part of the program involving reading from STDIN and writing to STDOUT has been provided by us.

public class Solution {
   static BufferedReader in = new BufferedReader(new InputStreamReader(
         System.in));
   static StringBuilder out = new StringBuilder();

   public static void main(String[] args) throws NumberFormatException, IOException {
      int numPackets = Integer.parseInt(in.readLine());
      int numKids = Integer.parseInt(in.readLine());
      int[] packets = new int[numPackets];

      for(int i = 0; i < numPackets; i ++)
      {
         packets[i] = Integer.parseInt(in.readLine());
      }

      int unfairness = Integer.MAX_VALUE;

      Arrays.sort(packets);
      int first = 0;
      int k = numKids - 1;
      int min = -1;
      while (k < numPackets){
          if (min == -1){
              min = packets[k] - packets[first];
          }else{
              min = Math.min(min, packets[k]-packets[first]);
          }
          first++;
          k++;
      }
      unfairness = min;
      System.out.println(unfairness);
   }
}
