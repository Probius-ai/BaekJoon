

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q11660 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int qNum = Integer.parseInt(st.nextToken());

        long arr[][] = new long[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long sumArr[][] = new long[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                sumArr[i][j] = sumArr[i - 1][j] + sumArr[i][j - 1] - sumArr[i - 1][j - 1] + arr[i][j];
            }
        }

        for (int i = 0; i < qNum; i++) {
            st = new StringTokenizer(br.readLine());
            int startIdx = Integer.parseInt(st.nextToken());
            int startIdy = Integer.parseInt(st.nextToken());
            int endIdx = Integer.parseInt(st.nextToken());
            int endIdy = Integer.parseInt(st.nextToken());
            System.out.println(sumArr[endIdx][endIdy] - sumArr[startIdx-1][endIdy] - sumArr[endIdx][startIdy-1] + sumArr[startIdx-1][startIdy-1]);
        }
    }
}