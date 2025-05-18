import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int count = 0;
    static int[] queen;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        queen = new int[N]; // 인덱스는 행, 값은 열 의미

        backtrack(0);
        System.out.println(count);
    }

    static void backtrack(int row) {
        if (row == N) {
            count++;
            return;
        }

        for (int col = 0; col < N; col++) {
            if (isValid(row, col)) {
                queen[row] = col;
                backtrack(row + 1);
            }
        }
    }

    static boolean isValid(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (queen[i] == col || Math.abs(row - i) == Math.abs(col - queen[i])) {
                return false;
            }
        }
        return true;
    }
}
