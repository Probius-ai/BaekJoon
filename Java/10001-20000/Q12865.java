import java.util.Scanner;

public class Q12865 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Your code goes here
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] W = new int[N];
        int[] V = new int[N];

        for (int i = 0; i < N; i++) {
            W[i] = sc.nextInt();
            V[i] = sc.nextInt();
        }
        


        sc.close();
    }
}