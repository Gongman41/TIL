
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
// 아 이거 어디서 봤는데. 아 풀었었는데. 
// 숫자의 크기, 갯수. 갱신. 갯수가 같으면 작은수로. 
public class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] dpUp = new int[n];   // 증가
        int[] dpDown = new int[n]; // 감소
        
        // 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        // 증가 부분 수열 계산 (앞에서부터)
        for (int i = 0; i < n; i++) {
            dpUp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    dpUp[i] = Math.max(dpUp[i], dpUp[j] + 1);
                }
            }
        }
        // 각 인덱스마다 거기까지 증가 개수 저장
        // 아래는 그 반대. 그리고 합한 애들중에 가장 큰 거 출력.
        // 감소 부분 수열 계산 (뒤에서부터)
        for (int i = n - 1; i >= 0; i--) {
            dpDown[i] = 1;
            for (int j = n - 1; j > i; j--) {
                if (arr[j] < arr[i]) {
                    dpDown[i] = Math.max(dpDown[i], dpDown[j] + 1);
                }
            }
        }
        
        // 정답 계산
        int max = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, dpUp[i] + dpDown[i] - 1);
        }
        
        System.out.println(max);
        
    }
}
