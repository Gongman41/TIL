import java.util.Scanner;

public class Main {
    static final long MOD = 1000000007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        long result = 0;

        for (int i = 0; i < M; i++) {
            long B = sc.nextLong();  // 분모
            long A = sc.nextLong();  // 분자

            long inverseB = modInverse(B, MOD);  // B의 모듈러 역수
            long term = (A * inverseB) % MOD;    // A * B^(-1) mod MOD
            result = (result + term) % MOD;
        }

        System.out.println(result);
    }

    // 모듈러 역수 구하기: b^(MOD-2) % MOD (페르마의 소정리)
    public static long modInverse(long b, long mod) {
        return power(b, mod - 2, mod);
    }

    // 빠른 거듭제곱 (Binary Exponentiation)
    public static long power(long base, long exp, long mod) {
        long result = 1;
        base %= mod;

        while (exp > 0) {
            if ((exp & 1) == 1) {  // 홀수면 곱하기
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;  // exp /= 2
        }

        return result;
    }
}
