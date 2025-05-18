import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// public class Main {
//     static int N;
//     static int[][] map;
//     static int cnt = 0;

//     // 방향 정의: 0=가로, 1=세로, 2=대각선
//     static class Pipe {
//         int x, y, dir;

//         Pipe(int x, int y, int dir) {
//             this.x = x;
//             this.y = y;
//             this.dir = dir;
//         }
//     }

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         N = Integer.parseInt(br.readLine());
//         map = new int[N][N];

//         for (int i = 0; i < N; i++) {
//             StringTokenizer st = new StringTokenizer(br.readLine());
//             for (int j = 0; j < N; j++) {
//                 map[i][j] = Integer.parseInt(st.nextToken());
//             }
//         }

//         bfs();
//         System.out.println(cnt);
//     }

//     static void bfs() {
//         Queue<Pipe> queue = new LinkedList<>();
//         // 시작 파이프: (0,1) 머리, 가로 방향
//         queue.add(new Pipe(0, 1, 0));

//         while (!queue.isEmpty()) {
//             Pipe p = queue.poll();
//             int x = p.x;
//             int y = p.y;
//             int dir = p.dir;

//             if (x == N - 1 && y == N - 1) {
//                 cnt++;
//                 continue;
//             }

//             // 가로
//             if (dir == 0 || dir == 2) {
//                 if (canMove(x, y + 1))
//                     queue.add(new Pipe(x, y + 1, 0));
//             }

//             // 세로
//             if (dir == 1 || dir == 2) {
//                 if (canMove(x + 1, y))
//                     queue.add(new Pipe(x + 1, y, 1));
//             }

//             // 대각선
//             if (canMove(x + 1, y) && canMove(x, y + 1) && canMove(x + 1, y + 1)) {
//                 queue.add(new Pipe(x + 1, y + 1, 2));
//             }
//         }
//     }

//     static boolean canMove(int x, int y) {
//         return x < N && y < N && map[x][y] == 0;
//     }
// }

// 시간초과 남

public class Main {
    static int N, result = 0;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, 1, 0);  // (0,0)-(0,1)에서 시작, 방향 가로(0)
        System.out.println(result);
    }

    static void dfs(int x, int y, int dir) {
        if (x == N - 1 && y == N - 1) {
            result++;
            return;
        }

        // 가로일 때: →, ↘
        if (dir == 0 || dir == 2) {
            if (y + 1 < N && map[x][y + 1] == 0) {
                dfs(x, y + 1, 0);
            }
        }

        // 세로일 때: ↓, ↘
        if (dir == 1 || dir == 2) {
            if (x + 1 < N && map[x + 1][y] == 0) {
                dfs(x + 1, y, 1);
            }
        }

        // 대각선일 때: ↘ (모든 경우에서 시도)
        if (x + 1 < N && y + 1 < N &&
            map[x][y + 1] == 0 && map[x + 1][y] == 0 && map[x + 1][y + 1] == 0) {
            dfs(x + 1, y + 1, 2);
        }
    }
}

// import java.io.*;
// import java.util.*;

// public class Main {
//     static int N;
//     static int[][] map;
//     static int[][][] dp;

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         N = Integer.parseInt(br.readLine());
//         map = new int[N][N];
//         dp = new int[N][N][3];

//         for (int i = 0; i < N; i++) {
//             StringTokenizer st = new StringTokenizer(br.readLine());
//             for (int j = 0; j < N; j++) {
//                 map[i][j] = Integer.parseInt(st.nextToken());
//             }
//         }

//         // 시작 위치: (0, 1) 가로 방향
//         dp[0][1][0] = 1;

//         for (int x = 0; x < N; x++) {
//             for (int y = 0; y < N; y++) {
//                 if (map[x][y] == 1) continue; // 벽이면 pass

//                 // 가로 -> (→), (↘)
//                 if (y - 1 >= 0) {
//                     dp[x][y][0] += dp[x][y - 1][0] + dp[x][y - 1][2];
//                 }

//                 // 세로 -> (↓), (↘)
//                 if (x - 1 >= 0) {
//                     dp[x][y][1] += dp[x - 1][y][1] + dp[x - 1][y][2];
//                 }

//                 // 대각선 -> (↘)
//                 if (x - 1 >= 0 && y - 1 >= 0 &&
//                     map[x - 1][y] == 0 && map[x][y - 1] == 0) {
//                     dp[x][y][2] += dp[x - 1][y - 1][0] + dp[x - 1][y - 1][1] + dp[x - 1][y - 1][2];
//                 }
//             }
//         }

//         int result = dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2];
//         System.out.println(result);
//     }
// }

// dp방식