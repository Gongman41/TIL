import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] dist;
    static final int INF = 100000000; // 충분히 큰 값

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        dist = new int[N + 1][N + 1];

        // 초기화: 자기 자신은 0, 나머지는 INF
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i == j) dist[i][j] = 0;
                else dist[i][j] = INF;
            }
        }

        // 입력 처리: 같은 노선 중 더 짧은 비용만 저장
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            dist[a][b] = Math.min(dist[a][b], c);
        }

        // 플로이드 워셜 알고리즘
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                    // 어디를 가는 데 경유해서 가는 게 나으면 경유.
                    // 여러 곳 경유하는 것도 그 최솟값이 다 저장되어있기때문에 적용
                }
            }
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (dist[i][j] == INF) sb.append("0 ");
                else sb.append(dist[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
// import java.io.*;
// import java.util.*;

// public class Main {
//     static final int INF = 1_000_000_000;
//     static int N, M;
//     static List<Node>[] graph;
//     static int[][] dist;

//     static class Node implements Comparable<Node> {
//         int to, cost;

//         public Node(int to, int cost) {
//             this.to = to;
//             this.cost = cost;
//         }

//         public int compareTo(Node o) {
//             return this.cost - o.cost;
//         }
//     }

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         N = Integer.parseInt(br.readLine());
//         M = Integer.parseInt(br.readLine());

//         graph = new ArrayList[N + 1];
//         dist = new int[N + 1][N + 1];

//         for (int i = 1; i <= N; i++) {
//             graph[i] = new ArrayList<>();
//             Arrays.fill(dist[i], INF);
//         }

//         for (int i = 0; i < M; i++) {
//             StringTokenizer st = new StringTokenizer(br.readLine());
//             int from = Integer.parseInt(st.nextToken());
//             int to = Integer.parseInt(st.nextToken());
//             int cost = Integer.parseInt(st.nextToken());

//             // 같은 노선이 여러 번 주어질 수 있으므로 더 작은 비용만 저장
//             graph[from].add(new Node(to, cost));
//         }

//         // 모든 정점에서 다익스트라 수행
//         for (int i = 1; i <= N; i++) {
//             dijkstra(i);
//         }

//         // 출력
//         StringBuilder sb = new StringBuilder();
//         for (int i = 1; i <= N; i++) {
//             for (int j = 1; j <= N; j++) {
//                 if (i == j || dist[i][j] == INF) sb.append("0 ");
//                 else sb.append(dist[i][j]).append(" ");
//             }
//             sb.append("\n");
//         }
//         System.out.print(sb);
//     }

//     static void dijkstra(int start) {
//         PriorityQueue<Node> pq = new PriorityQueue<>();
//         pq.add(new Node(start, 0));
//         dist[start][start] = 0;

//         while (!pq.isEmpty()) {
//             Node now = pq.poll();
//             int cur = now.to;
//             int curCost = now.cost;

//             if (curCost > dist[start][cur]) continue;

//             for (Node next : graph[cur]) {
//                 if (dist[start][next.to] > dist[start][cur] + next.cost) {
//                     dist[start][next.to] = dist[start][cur] + next.cost;
//                     pq.add(new Node(next.to, dist[start][next.to]));
//                 }
//             }
//         }
//     }
// }
