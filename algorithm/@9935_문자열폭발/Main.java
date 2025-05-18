import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();       // 원본 문자열
        String bomb = br.readLine();      // 폭탄 문자열
        StringBuilder result = new StringBuilder();
//  StringBuilder는 문자열 전용 스택같은 느낌.문자길이는 length
        int bombLength = bomb.length();

        for (int i = 0; i < str.length(); i++) {
            result.append(str.charAt(i)); // 하나씩 추가
            // 문자열.charAt(인덱스)

            // 폭탄 문자열과 길이가 같거나 클 때만 비교 가능
            if (result.length() >= bombLength) {
                // 끝에서 bomb 길이만큼 잘라서 비교
                if (result.substring(result.length() - bombLength).equals(bomb)) {
                    // substring 알아두기
                    result.delete(result.length() - bombLength, result.length());
                }
            }
        }

        // 결과 출력
        System.out.println(result.length() == 0 ? "FRULA" : result.toString());
    }
}
