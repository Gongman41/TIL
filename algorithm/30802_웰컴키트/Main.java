import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine()); // 참가자 수
        int[] sizes = new int[6]; // S, M, L, XL, XXL, XXXL
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 6; i++) {
            sizes[i] = Integer.parseInt(st.nextToken());
        }
        
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken()); // 티셔츠 묶음 수
        int P = Integer.parseInt(st.nextToken()); // 펜 묶음 수
        
        int shirtBundles = 0;
        for (int size : sizes) {
            shirtBundles += (size + T - 1) / T; // 올림 계산
        }
        
        int penBundles = N / P;
        int penSingles = N % P;
        
        System.out.println(shirtBundles);
        System.out.println(penBundles + " " + penSingles);
    }
}
