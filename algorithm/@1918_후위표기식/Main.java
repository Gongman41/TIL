import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static int getPriority(char op) {
        if (op == '(') return 0;
        if (op == '+' || op == '-') return 1;
        if (op == '*' || op == '/') return 2;
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String infix = br.readLine();
        StringBuilder postfix = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < infix.length(); i++) {
            char ch = infix.charAt(i);

            if (Character.isAlphabetic(ch)) {
                // 피연산자는 바로 출력
                postfix.append(ch);
            } else if (ch == '(') {
                stack.push(ch);
            } else if (ch == ')') {
                // 여는 괄호 만날 때까지 pop
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfix.append(stack.pop());
                }
                stack.pop(); // '(' 제거
            } else {
                // 연산자일 경우 우선순위 고려하여 pop
                while (!stack.isEmpty() && getPriority(stack.peek()) >= getPriority(ch)) {
                    postfix.append(stack.pop());
                }
                // 그전까지는 바로 바로 pop하거나 순서맞으면 냅뒀다가 pop하거나. 괄호나오면 
                stack.push(ch);
            }
        }

        // 남은 연산자 출력
        while (!stack.isEmpty()) {
            postfix.append(stack.pop());
        }

        System.out.println(postfix);
    }
}
