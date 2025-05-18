import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

// 역시 완탐. 근데 bfs는 아니었다. 그냥 받아서 따로 저장. 이게 맞는듯.

public class Main {

    static int N, M;
    static List<int[]> houses = new ArrayList<>();
    // 가변적인 크기. List는 인터페이스고 ArrayList는 그것의 구현체
    static List<int[]> chickens = new ArrayList<>();
    static boolean[] selected;
    static int minDistance = Integer.MAX_VALUE;
// 메서드 사용 시 사용될 변수들은 static으로 선언해줘야됨
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 도시 정보 입력
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int value = Integer.parseInt(st.nextToken());
                if (value == 1) houses.add(new int[]{i, j});
                else if (value == 2) chickens.add(new int[]{i, j});
            }
        }

        selected = new boolean[chickens.size()];
        dfs(0, 0);
        System.out.println(minDistance);
    }

    // 조합 생성 (치킨집 M개 선택)
    static void dfs(int start, int count) {
        if (count == M) {
            minDistance = Math.min(minDistance, calcDistance());
            return;
        }

        for (int i = start; i < chickens.size(); i++) {
            selected[i] = true;
            dfs(i + 1, count + 1);
            selected[i] = false;
        }
    }

    // 도시의 치킨 거리 계산
    static int calcDistance() {
        int total = 0;

        for (int[] house : houses) {
            // 아 이런식으로
            int hx = house[0], hy = house[1];
            int min = Integer.MAX_VALUE;

            for (int i = 0; i < chickens.size(); i++) {
                if (selected[i]) {
                    int[] chick = chickens.get(i);
                    int cx = chick[0], cy = chick[1];
                    int dist = Math.abs(hx - cx) + Math.abs(hy - cy);
                    min = Math.min(min, dist);
                }
            }

            total += min;
        }

        return total;
    }
}
