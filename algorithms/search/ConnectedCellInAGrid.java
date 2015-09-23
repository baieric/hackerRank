import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

// Solution to https://www.hackerrank.com/challenges/connected-cell-in-a-grid

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int rows = in.nextInt();
        int cols = in.nextInt();
        int[][] grid = new int[rows][cols];
        boolean[][] seen = new boolean[rows][cols];
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                grid[i][j] = in.nextInt();
                seen[i][j] = false;
            }
        }
        int max = 0;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                int size = FloodFillDFS(i, j, rows, cols, grid, seen);
                if(size > max){
                    max = size;
                }
            }
        }
        System.out.println(max);
    }

    public static int FloodFillDFS(int x, int y, int rows, int cols, int[][] grid, boolean[][] seen) {
        if (x < 0 || x >= rows || y < 0 || y >= cols) {
            return 0;
        }
        if (seen[x][y]) {
            return 0;
        }
        seen[x][y] = true;
        if (grid[x][y] == 0) {
            return 0;
        }
        int sum = 1;
        sum += FloodFillDFS(x + 1, y, rows, cols, grid, seen);
        sum += FloodFillDFS(x - 1, y, rows, cols, grid, seen);
        sum += FloodFillDFS(x, y + 1, rows, cols, grid, seen);
        sum += FloodFillDFS(x, y - 1, rows, cols, grid, seen);
        sum += FloodFillDFS(x- 1, y - 1, rows, cols, grid, seen);
        sum += FloodFillDFS(x + 1, y + 1, rows, cols, grid, seen);
        sum += FloodFillDFS(x - 1, y + 1, rows, cols, grid, seen);
        sum += FloodFillDFS(x + 1, y - 1, rows, cols, grid, seen);
        return sum;
    }
}
