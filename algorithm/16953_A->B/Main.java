import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {  // 클래스 이름은 M
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        String a = input[0];
        String b = input[1];

        int count = 1;  // 시작값 포함
        while (true) {
            if (b.equals(a)) {
                System.out.println(count);
                break;
            }

            if (b.endsWith("1")) {
                b = b.substring(0, b.length() - 1);  // 마지막 문자 제거
                count++;
            } else if (b.matches("\\d+") && Long.parseLong(b) % 2 == 0) {
                b = String.valueOf(Long.parseLong(b) / 2);
                count++;
            } else {
                System.out.println(-1);
                break;
            }
        }
    }
}
