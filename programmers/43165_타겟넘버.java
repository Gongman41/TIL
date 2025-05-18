class Solution {
    static int N;
    static int cnt = 0;
    public static void dfs(int[]numbers,int cur,int i, int target){
        if(i == N){
            if(cur == target) cnt += 1;
            return;
        }
        dfs(numbers,cur+numbers[i],i+1,target);
        dfs(numbers,cur-numbers[i],i+1,target);
    }
    public int solution(int[] numbers, int target) {
        N = numbers.length;
        dfs(numbers,0,0,target);
        return cnt;
    }
}