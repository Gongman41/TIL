
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
public class Main {
    static int N;
    static int M;
    static int[][] map;
    static int max = 0;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    // BFS. 상하좌우 대각선 체크하고 가는 거 생각해봤는데 아닌듯.
    // 좀더 멀리꺼까지 생각. 3x3. 근데 개수가 3개임. 그럼 돌다가 안될거같으면 버려야됨
    // 그럼 그냥 빈칸에 3번 벽놓는 경우를 생각해야되나
// 3<=N,M<=8, 2 <= 바이러스개수<=10
// 바이러스마다 몇개로 막을 수 있는 지 벽개수, 바이러스 점령개수 이렇게 놓으면?
// ㅁㅊ 완탐이었네
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        for(int i = 0;i < N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0;j < M;j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0);
        System.out.println(max);


        
    }

    static void dfs(int count){
        if(count == 3){
            spreadVirus();
            return;
        }

        for(int i = 0; i < N; i++) {
            for(int j = 0;j< M;j++){
                if(map[i][j] == 0){
                    map[i][j] = 1;
                    dfs(count + 1);
                    map[i][j] = 0;
                }
            }
        }
    }

    static void spreadVirus(){
            int[][] temp = new int[N][M];
            for(int i = 0; i < N; i++){
                temp[i] = map[i].clone();
                // clone 깊은 복사.
            }
    
            Queue<int[]> q = new LinkedList<>();
            for(int i = 0; i < N; i++){
                for(int j = 0; j < M; j++){
                    if(temp[i][j] == 2){
                        q.offer(new int[]{i, j});
                    }
                }
            }
    
            while(!q.isEmpty()){
                int[] cur = q.poll();
                for(int d = 0; d < 4; d++){
                    int nx = cur[0] + dx[d];
                    int ny = cur[1] + dy[d];
    
                    if(nx >= 0 && ny >= 0 && nx < N && ny < M){
                        if(temp[nx][ny] == 0){
                            temp[nx][ny] = 2;
                            q.offer(new int[]{nx, ny});
                        }
                    }
                }
            }
    
            // 안전영역 계산
            int safe = 0;
            for(int i = 0; i < N; i++){
                for(int j = 0; j < M; j++){
                    if(temp[i][j] == 0){
                        safe++;
                    }
                }
            }
    
            max = Math.max(max, safe);
        }


}
