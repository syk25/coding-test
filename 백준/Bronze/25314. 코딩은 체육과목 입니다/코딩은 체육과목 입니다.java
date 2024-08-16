import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int q = N / 4;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < q; i++){
            sb.append("long ");
        }
        sb.append("int");
        String answer = sb.toString();
        System.out.println(answer);
    }
}