import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    int N;
    boolean[][] visited;
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    public int solution(int[][] game_board, int[][] table) {
        N = game_board.length;
        List<int[][]> blanks = new ArrayList<>();
        List<int[][]> blocks = new ArrayList<>();

        // 1. game_board에서 빈칸(0)의 모양 추출
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j] && game_board[i][j] == 0) {
                    blanks.add(extractShape(i, j, game_board, 0));
                }
            }
        }

        // 2. table에서 블럭(1)의 모양 추출
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j] && table[i][j] == 1) {
                    blocks.add(extractShape(i, j, table, 1));
                }
            }
        }

        // 3. 매칭 과정
        boolean[] used = new boolean[blocks.size()];
        int answer = 0;

        for (int[][] blank : blanks) {
            for (int k = 0; k < blocks.size(); k++) {
                if (used[k]) continue;
                int[][] block = blocks.get(k);

                for (int r = 0; r < 4; r++) {
                    if (isSame(blank, block)) {
                        answer += countOnes(block);
                        used[k] = true;
                        break;
                    }
                    block = rotate(block); // 90도 회전
                }

                if (used[k]) break;
            }
        }

        return answer;
    }

    // BFS로 블록 모양 추출 (2차원 배열로)
    int[][] extractShape(int x, int y, int[][] board, int target) {
        List<int[]> shapeList = new ArrayList<>();
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;
        int minX = x, minY = y, maxX = x, maxY = y;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cx = cur[0], cy = cur[1];
            shapeList.add(new int[]{cx, cy});
            minX = Math.min(minX, cx);
            minY = Math.min(minY, cy);
            maxX = Math.max(maxX, cx);
            maxY = Math.max(maxY, cy);
            for (int d = 0; d < 4; d++) {
                int nx = cx + dr[d];
                int ny = cy + dc[d];
                if (0 <= nx && nx < N && 0 <= ny && ny < N &&
                        !visited[nx][ny] && board[nx][ny] == target) {
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny});
                }
            }
        }

        int[][] shape = new int[maxX - minX + 1][maxY - minY + 1];
        for (int[] p : shapeList) {
            shape[p[0] - minX][p[1] - minY] = 1;
        }

        return shape;
    }

    // 도형 회전 (90도 회전)
    int[][] rotate(int[][] shape) {
        int row = shape.length;
        int col = shape[0].length;
        int[][] rotated = new int[col][row];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                rotated[j][row - 1 - i] = shape[i][j];
            }
        }
        return rotated;
    }

    // 두 도형이 같은지 확인
    boolean isSame(int[][] a, int[][] b) {
        if (a.length != b.length || a[0].length != b[0].length) return false;
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length; j++) {
                if (a[i][j] != b[i][j]) return false;
            }
        }
        return true;
    }

    // 도형에서 1의 개수 세기
    int countOnes(int[][] shape) {
        int count = 0;
        for (int[] row : shape) {
            for (int val : row) {
                if (val == 1) count++;
            }
        }
        return count;
    }
}
