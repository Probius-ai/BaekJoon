import java.util.Scanner; 

/**
 * Q11659
 */
public class Q11659 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int Arrays[] = new int[N];
        for(int i=0;i<N;i++){
            Arrays[i] = sc.nextInt();
        }

        int S_list[] = new int[N+1];
        for(int i =1;i<=N;i++){
            S_list[i]=S_list[i-1]+Arrays[i-1];
        }
        int result;
        for(int k=0; k<M;k++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            
            result = S_list[j]-S_list[i-1];
            System.out.println(result);
        }
    }
}