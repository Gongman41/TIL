class Solution {
    public int solution(int[][] triangle) {
        int N = triangle.length;
        int[][] dp = new int[N][];
        
        // 깊은 복사 (deep copy)
        for (int i = 0; i < N; i++) {
            dp[i] = triangle[i].clone();
        }

        // 아래에서 위로 누적합
        for (int i = N - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                dp[i][j] += Math.max(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }

        return dp[0][0];
    }
}

// class Solution {
//     public int solution(int[][] triangle) {
//         int N = triangle.length;
//         int[][] dp = new int[N][];
        
//         // 깊은 복사 (Deep Copy)
//         for (int i = 0; i < N; i++) {
//             dp[i] = triangle[i].clone();
//         }

//         for (int i = 0; i < N - 1; i++) {
//             for (int j = 0; j < triangle[i].length; j++) {
//                 // 다음 행의 j 위치
//                 dp[i + 1][j] = Math.max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j]);

//                 // 다음 행의 j+1 위치
//                 dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1]);
//             }
//         }

//         // 마지막 행에서 최대값 반환
//         int max = 0;
//         for (int num : dp[N - 1]) {
//             max = Math.max(max, num);
//         }

//         return max;
//     }
// }

