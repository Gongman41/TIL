import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스 개수 입력 받기

        // 최대 n이 10이므로 미리 dp 배열을 계산해 둠
        int[] dp = new int[11]; // n이 1~10이므로 크기를 11로 설정 (dp[0]은 사용하지 않음)
        dp[1] = 1; // 1을 만드는 경우의 수 -> (1)
        dp[2] = 2; // 2를 만드는 경우의 수 -> (1+1, 2)
        dp[3] = 4; // 3을 만드는 경우의 수 -> (1+1+1, 1+2, 2+1, 3)

        // DP 테이블 채우기
        for (int i = 4; i <= 10; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }

        // 테스트 케이스 처리
        while (T-- > 0) {
            int n = sc.nextInt(); // 테스트 케이스마다 n 입력 받기
            System.out.println(dp[n]); // 미리 계산된 dp[n] 출력
        }

        sc.close(); // Scanner 닫기
    }
}
