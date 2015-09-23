import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/the-time-in-words

// Note: only needed to map one through twenty

public class Solution {
    private static final String[] numNames = { "", "one", "two", "three",
            "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen", "twenty" };

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int hour;
        hour = in.nextInt();
        int min;
        min = in.nextInt();

        if(min == 0){
            System.out.println(numNames[hour] + " o' clock");
        }else if(min == 15){
            System.out.println("quarter past " + numNames[hour]);
        }else if(min == 30){
            System.out.println("half past " + numNames[hour]);
        }else if(min == 45){
            int next = hour == 12 ? 1 : hour + 1;
            System.out.println("quarter to " + numNames[next]);
        } else if(min < 30){
            String word;
            if(min > 20){
                word = "twenty " + numNames[min % 20];
            }else{
                word = numNames[min];
            }
            System.out.println(word + " minutes past " + numNames[hour]);
        } else{
            String word;
            int num = 60 - min;
            if(num > 20){
                word = "twenty " + numNames[num % 20];
            }else{
                word = numNames[num];
            }
            int next = hour == 12 ? 1 : hour + 1;
            System.out.println(word + " minutes to " + numNames[next]);
        }
    }
}
