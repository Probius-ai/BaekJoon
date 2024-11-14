package Java;
import java.util.Scanner;
/**
 * Q.1057
 */
public class Q.1057 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        if(N==M){
            System.out.println(1);
        } else{
            System.out.print(0);
        }
    }
}