import java.util.Stack;

class Solution {
    // 올바른 괄호 문자열인지 확인
    public static boolean isCorrect(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(') stack.push(ch);
            else {
                if (stack.isEmpty()) return false;
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    // u, v 분리 지점 찾기
    public static int splitIndex(String s) {
        int left = 0, right = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') left++;
            else right++;
            if (left == right) return i + 1; // 자를 때 오른쪽 포함이므로 +1
        }
        return s.length();
    }

    // 메인 재귀 함수
    public static String convert(String p) {
        if (p.isEmpty()) return "";

        int index = splitIndex(p);
        String u = p.substring(0, index);
        String v = p.substring(index);

        if (isCorrect(u)) {
            return u + convert(v);
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append('(');
            sb.append(convert(v));
            sb.append(')');

            // u의 첫/마지막 문자 제거 후 괄호 뒤집기
            for (int i = 1; i < u.length() - 1; i++) {
                sb.append(u.charAt(i) == '(' ? ')' : '(');
            }

            return sb.toString();
        }
    }

    public String solution(String p) {
        return convert(p);
    }
}
