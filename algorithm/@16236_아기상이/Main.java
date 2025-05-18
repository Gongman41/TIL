import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 0, 1}; // 위, 왼, 오, 아래
    static int[] dy = {0, -1, 1, 0};
    static int sharkSize = 2;
    static int eatCount = 0;
    static int time = 0;
    static int sx, sy; // 상어 위치

    static class Fish implements Comparable<Fish> {
        int x, y, dist;
        public Fish(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
        @Override
        public int compareTo(Fish o) {
            if (this.dist == o.dist) {
                if (this.x == o.x) return this.y - o.y;
                return this.x - o.x;
            }
            return this.dist - o.dist;
        }
    }
// 큐랑 우선순위 큐 같이쓰기
    public static Fish bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        visited = new boolean[N][N];
        PriorityQueue<Fish> fishList = new PriorityQueue<>();

        queue.offer(new int[]{x, y, 0});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cx = cur[0];
            int cy = cur[1];
            int dist = cur[2];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (visited[nx][ny] || map[nx][ny] > sharkSize) continue;

                visited[nx][ny] = true;

                if (map[nx][ny] > 0 && map[nx][ny] < sharkSize) {
                    fishList.offer(new Fish(nx, ny, dist + 1));
                }

                queue.offer(new int[]{nx, ny, dist + 1});
            }
        }

        return fishList.isEmpty() ? null : fishList.poll();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 9) {
                    sx = i;
                    sy = j;
                    map[i][j] = 0;
                }
            }
        }

        while (true) {
            Fish target = bfs(sx, sy);
            if (target == null) break;

            time += target.dist;
            sx = target.x;
            sy = target.y;
            map[sx][sy] = 0;
            eatCount++;

            if (eatCount == sharkSize) {
                sharkSize++;
                eatCount = 0;
            }
        }

        System.out.println(time);
    }
}
