import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 행렬 거듭제곱이라는 데 처음봄
public class Main {
    static final long MOD = 1_000_000_007L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());

        long[][] result = fib(n);
        System.out.println(result[0][1]); // F(n)
    }

    // 피보나치 수를 구하는 행렬 빠른 제곱
    static long[][] fib(long n) {
        if (n == 0) return new long[][]{{0, 0}, {0, 0}};
        if (n == 1) return new long[][]{{1, 1}, {1, 0}};

        long[][] half = fib(n / 2);
        long[][] squared = multiply(half, half);

        if (n % 2 == 0) {
            return squared;
        } else {
            return multiply(squared, new long[][]{{1, 1}, {1, 0}});
        }
    }

    // 행렬 곱셈
    static long[][] multiply(long[][] a, long[][] b) {
        long[][] result = new long[2][2];

        result[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD;
        result[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD;
        result[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD;
        result[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD;

        return result;
    }
}
