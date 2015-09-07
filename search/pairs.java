import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/domains/algorithms/search

// Fun fact: I got an almost identical question in my interview for D2L,
// and I ended up landing the job

public class Solution {
    static int pairs(int[] a,int k) {
        Set nums = new HashSet();
        int answer = 0;
        for (int i = 0; i < a.length; i++){
            nums.add(a[i]);
        }
        for (int i = 0; i < a.length; i++){
            if (nums.contains(a[i]-k)){
                answer++;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int res;

        String n = in.nextLine();
        String[] n_split = n.split(" ");

        int _a_size = Integer.parseInt(n_split[0]);
        int _k = Integer.parseInt(n_split[1]);

        int[] _a = new int[_a_size];
        int _a_item;
        String next = in.nextLine();
        String[] next_split = next.split(" ");

        for(int _a_i = 0; _a_i < _a_size; _a_i++) {
            _a_item = Integer.parseInt(next_split[_a_i]);
            _a[_a_i] = _a_item;
        }

        res = pairs(_a,_k);
        System.out.println(res);
    }
}
