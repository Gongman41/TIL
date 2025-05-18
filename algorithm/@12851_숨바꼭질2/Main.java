import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[] time = new int[100001]; // 해당 위치까지 걸린 시간
    static int[] count = new int[100001]; // 해당 위치까지 도달하는 방법의 수

    // 그냥 방문처리를 하는게 아니라 방문처리하면서 횟수 갱신. 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        bfs(N);

        System.out.println(time[K]);
        System.out.println(count[K]);
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        time[start] = 0;
        count[start] = 1;

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int next : new int[]{now - 1, now + 1, now * 2}) {
                if (next < 0 || next > 100000) continue;

                // 처음 방문하는 경우
                if (time[next] == 0 && next != N) {
                    time[next] = time[now] + 1;
                    count[next] = count[now];
                    q.add(next);
                }
                // 이미 방문했지만 같은 시간에 도착한 경우 → 방법의 수 누적
                else if (time[next] == time[now] + 1) {
                    count[next] += count[now];
                }
            }
        }
    }
}
