import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] A, B;

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 처리
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        B = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> answer = new ArrayList<>();
        int i = 0, j = 0;

        while (true) {
            int max = -1;
            int ni = -1, nj = -1;

            // 공통 원소 중 가장 큰 값을 찾음
            for (int a = i; a < N; a++) {
                for (int b = j; b < M; b++) {
                    if (A[a] == B[b] && A[a] > max) {
                        max = A[a];
                        ni = a;
                        nj = b;
                    }
                }
            }

            // 더 이상 공통 원소가 없으면 종료
            if (max == -1) break;

            answer.add(max);
            i = ni + 1;
            j = nj + 1;
        }

        // 출력
        System.out.println(answer.size());
        for (int val : answer) {
            System.out.print(val + " ");
        }
    }
}
