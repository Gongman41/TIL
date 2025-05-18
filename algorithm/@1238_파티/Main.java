import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
// 그냥 다익스트라가 아니라 역방향 그래프를 만들어야되는 다익스트라...
public class Main {
    static class Node implements Comparable<Node> {
        int to, cost;
        public Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    static int N, M, X;
    static List<Node>[] graph, reverseGraph;

// 다익스트라는 노드 별 길이 visited처럼 해줘야됨
    static int[] dijkstra(List<Node>[] g, int start) {
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (dist[cur.to] < cur.cost) continue;
            for (Node next : g[cur.to]) {
                if (dist[next.to] > cur.cost + next.cost) {
                    dist[next.to] = cur.cost + next.cost;
                    pq.offer(new Node(next.to, dist[next.to]));
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        reverseGraph = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
            reverseGraph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to   = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[from].add(new Node(to, cost));
            reverseGraph[to].add(new Node(from, cost)); // 역방향
        }

        int[] toX   = dijkstra(reverseGraph, X); // i → X
        int[] fromX = dijkstra(graph, X);        // X → i
// 이게 이해가 안가네.
// 원래 그래프의 모든 간선을 반대로 만든 역방향 그래프에서, X를 출발점으로 다익스트라 한 번만 돌리면,
// 사실상 i → X를 한 번에 구할 수 있습니다.
        int max = 0;
        for (int i = 1; i <= N; i++) {
            if (toX[i] != Integer.MAX_VALUE && fromX[i] != Integer.MAX_VALUE) {
                max = Math.max(max, toX[i] + fromX[i]);
            }
        }

        System.out.println(max);
    }
}
