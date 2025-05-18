import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] map;
    static int[][][] dist; // [x][y][벽 부쉈는지 여부]
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    // 배열에 두 경우 저장.
    static class Node {
        int x, y, broken;
        Node(int x, int y, int broken) {
            this.x = x;
            this.y = y;
            this.broken = broken; // 0이면 아직 안 부심, 1이면 부신 상태
        }
    }

    public static int bfs() {
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0, 0, 0));
        dist[0][0][0] = 1;

        while (!q.isEmpty()) {
            Node cur = q.poll();
            int x = cur.x;
            int y = cur.y;
            int broken = cur.broken;

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

                if (map[nx][ny] == 0 && dist[nx][ny][broken] == 0) {
                    dist[nx][ny][broken] = dist[x][y][broken] + 1;
                    q.add(new Node(nx, ny, broken));
                }

                if (map[nx][ny] == 1 && broken == 0 && dist[nx][ny][1] == 0) {
                    dist[nx][ny][1] = dist[x][y][broken] + 1;
                    q.add(new Node(nx, ny, 1));
                }
            }
        }

        int noBreak = dist[N-1][M-1][0];
        int breaked = dist[N-1][M-1][1];

        if (noBreak == 0 && breaked == 0) return -1;
        if (noBreak == 0) return breaked;
        if (breaked == 0) return noBreak;
        return Math.min(noBreak, breaked);
    }

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        dist = new int[N][M][2];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j) - '0';
            }
        }

        System.out.println(bfs());
    }
}
