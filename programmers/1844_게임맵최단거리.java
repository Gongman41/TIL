import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int[] row = {1, -1, 0, 0};
    static int[] col = {0, 0, 1, -1};
    static int[][] dist;

    public static void bfs(int[][] maps, int N, int[] start) {
        Queue<int[]> q = new LinkedList<>();
        q.add(start);
        dist[start[0]][start[1]] = 1;  // 시작 위치 초기화

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int nextR = cur[0] + row[i];
                int nextC = cur[1] + col[i];
                if (0 <= nextR && nextR < N && 0 <= nextC && nextC < maps[0].length
                        && maps[nextR][nextC] == 1
                        && dist[nextR][nextC] > dist[cur[0]][cur[1]] + 1) {
                    dist[nextR][nextC] = dist[cur[0]][cur[1]] + 1;
                    q.add(new int[]{nextR, nextC});
                }
            }
        }
    }

    public int solution(int[][] maps) {
        int N = maps.length;
        int M = maps[0].length;
        dist = new int[N][M];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], 1_000_000);
        }

        bfs(maps, N, new int[]{0, 0});

        int answer = dist[N - 1][M - 1];
        return answer == 1_000_000 ? -1 : answer;
    }
}
