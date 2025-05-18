import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static class Node implements Comparable<Node> {
        // Node 객체들끼리 크기 비교 가능_ 우선순위큐에서 정렬기준을 정하기위해 설정
        // 자바에서 직접 만든 객체를 우선순위큐에 넣으려면 비교기준이 있어야 정렬가능.
        int dest, cost;
        public Node(int dest, int cost) {
            this.dest = dest;
            this.cost = cost;
        }

        public int compareTo(Node o) {
            return this.cost - o.cost;
            // 내림차순을 원하면 반대로
        }
    }

    static final int INF = 200000000;
    // 값 봇바꿈
    static int N, E;
    static List<Node>[] graph;
    // 노드들을 가지는 배열_ 2차원배열.

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b, c));
            graph[b].add(new Node(a, c));
        }

        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());

        int[] distFrom1 = dijkstra(1);
        int[] distFromV1 = dijkstra(v1);
        int[] distFromV2 = dijkstra(v2);

        long path1 = (long)distFrom1[v1] + distFromV1[v2] + distFromV2[N];
        long path2 = (long)distFrom1[v2] + distFromV2[v1] + distFromV1[N];
        // 범위초과 우려
        long answer = Math.min(path1, path2);
        System.out.println(answer >= INF ? -1 : answer);
    }

    static int[] dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int[] dist = new int[N + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (dist[now.dest] < now.cost) continue;

            for (Node next : graph[now.dest]) {
                if (dist[next.dest] > dist[now.dest] + next.cost) {
                    dist[next.dest] = dist[now.dest] + next.cost;
                    pq.add(new Node(next.dest, dist[next.dest]));
                }
            }
        }
        return dist;
    }
}
