

// 진실아는 사람들 들어있는 파티를 전체 파티개수에서 빼면서, 그 안에 속해있는 다른 사람들도 따라가서 파티개수 빼기
// N개만큼 사람마다 속해있는 파티 배열 만들고, visited 파티배열 만들면?
// M만큼 돌다가 사람마다 파티저장, 그러다가 진실아는 사람 있는 파티 만나면 visited 처리. 
// 그리고 그 안에있는 사람 배열로 따라가서 파티 visited
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static List<Integer>[] parties;
    static List<Integer>[] people; // 사람별 파티 목록
    static boolean[] knowsTruth;
    static boolean[] visitedParty;
// 배열을 많이 만드는데
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // 사람 수
        M = Integer.parseInt(st.nextToken()); // 파티 수

        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken()); // 진실 아는 사람 수
        knowsTruth = new boolean[N + 1];

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < K; i++) {
            int person = Integer.parseInt(st.nextToken());
            knowsTruth[person] = true;
            queue.add(person); // 진실을 아는 사람부터 시작
        }

        // 각 파티에 누가 있는지 저장
        parties = new ArrayList[M];
        // 각 사람별로 어떤 파티에 들어있는지 저장
        people = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            people[i] = new ArrayList<>();
        }


        for (int i = 0; i < M; i++) {
            parties[i] = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            for (int j = 0; j < cnt; j++) {
                int person = Integer.parseInt(st.nextToken());
                parties[i].add(person);
                people[person].add(i); // 이 사람이 속한 파티 번호 기록
            }
        }

        // 진실을 아는 사람을 BFS로 퍼뜨리기
        visitedParty = new boolean[M];

        while (!queue.isEmpty()) {
            int current = queue.poll();
            for (int party : people[current]) {
                // 이거 문법 기억.
                if (visitedParty[party]) continue;
                visitedParty[party] = true;
                for (int nextPerson : parties[party]) {
                    if (!knowsTruth[nextPerson]) {
                        knowsTruth[nextPerson] = true;
                        queue.add(nextPerson);
                    }
                }
            }
        }

        // 이제 visitedParty == 진실이 퍼진 파티
        int answer = 0;
        for (int i = 0; i < M; i++) {
            if (!visitedParty[i]) answer++;
        }

        System.out.println(answer);
    }
}

// import java.io.*;
// import java.util.*;

// public class Main {
//     static int[] parent;
//     static boolean[] knowTruth;
//     static List<Integer>[] parties;

//     // find 함수 (경로 압축)
//     static int find(int x) {
//         if (parent[x] == x) return x;
//         return parent[x] = find(parent[x]);
//     }

//     // union 함수
//     static void union(int a, int b) {
//         int rootA = find(a);
//         int rootB = find(b);
//         if (rootA != rootB) {
//             parent[rootB] = rootA;
//         }
//     }

//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         StringTokenizer st = new StringTokenizer(br.readLine());

//         int N = Integer.parseInt(st.nextToken()); // 사람 수
//         int M = Integer.parseInt(st.nextToken()); // 파티 수

//         parent = new int[N + 1];
//         for (int i = 1; i <= N; i++) parent[i] = i;

//         knowTruth = new boolean[N + 1];
//         st = new StringTokenizer(br.readLine());
//         int T = Integer.parseInt(st.nextToken());

//         // 진실을 아는 사람 체크
//         for (int i = 0; i < T; i++) {
//             int person = Integer.parseInt(st.nextToken());
//             knowTruth[person] = true;
//         }

//         // 파티 정보 저장
//         parties = new ArrayList[M];
//         for (int i = 0; i < M; i++) {
//             st = new StringTokenizer(br.readLine());
//             int count = Integer.parseInt(st.nextToken());
//             parties[i] = new ArrayList<>();

//             int first = Integer.parseInt(st.nextToken());
//             parties[i].add(first);
//             for (int j = 1; j < count; j++) {
//                 int next = Integer.parseInt(st.nextToken());
//                 union(first, next);
//                 parties[i].add(next);
//             }
//         }

//         // 진실을 아는 사람과 같은 그룹으로 묶인 사람도 진실을 아는 것으로 간주
//         boolean[] groupKnowsTruth = new boolean[N + 1];
//         for (int i = 1; i <= N; i++) {
//             if (knowTruth[i]) {
//                 groupKnowsTruth[find(i)] = true;
//             }
//         }

//         int result = 0;
//         for (int i = 0; i < M; i++) {
//             boolean canLie = true;
//             for (int person : parties[i]) {
//                 if (groupKnowsTruth[find(person)]) {
//                     canLie = false;
//                     break;
//                 }
//             }
//             if (canLie) result++;
//         }

//         System.out.println(result);
//     }
// }
