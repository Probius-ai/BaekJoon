package Java;

import java.util.Arrays;
import java.util.Scanner;

public class Q1940 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int first = 0;
        int last = N-1;
        int count = 0;

        while (first < last) {
            int sum = arr[first] + arr[last];
            if (sum == M) {
                count++;
                first++;
                last--;
            } else if (sum < M) {
                first++;
            } else {
                last--;
            }
        }

        System.out.println(count);


        
    }


}
