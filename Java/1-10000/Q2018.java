package Java;

import java.util.Scanner;

public class Q2018 {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int ans = 1;
        int sum = 1;
        int top_pointer = 1;
        int bot_pointer = 1;

        while (top_pointer != num) {
            if (sum < num) {
                top_pointer++;
                sum += top_pointer;
            } else if (sum > num) {
                sum -= bot_pointer;
                bot_pointer++;
            } else {
                ans++;
                sum -= bot_pointer;
                bot_pointer++;
            }
        }
        System.out.println(ans);

        sc.close();
    }
}