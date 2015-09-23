
import java.util.*;

// Solution to https://www.hackerrank.com/challenges/flowers

class Solution{
   public static void main( String args[] ){
      Scanner in = new Scanner(System.in);

      int N, K;
      N = in.nextInt();
      K = in.nextInt();

      int C[] = new int[N];
      for(int i=0; i<N; i++){
         C[i] = in.nextInt();
      }

      Arrays.sort(C);
      int index = C.length - 1;
      int bought = 0;
      int result = 0;
      while(index >= 0){
          for(int i = 0; i < K; i++){
              if(index < 0) break;
              result += (bought + 1) * C[index];
              index--;
          }
          bought++;
      }
      System.out.println( result );
   }
}
