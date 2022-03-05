import java.io.BufferedInputStream;
import java.util.Scanner;

/**
 * @author Ryan Moyo
 * @date 2020/7/26 15:34
 */
public class CodeForces {
    public static void main(String[] args) {
        Scanner cin = new Scanner(new BufferedInputStream(System.in));
        long n = cin.nextLong();
        long m = cin.nextLong();
        long a = cin.nextLong();
        long ans1 = n / a + (n % a == 0 ? 0 : 1);
        long ans2 = m / a + (m % a == 0 ? 0 : 1);
        System.out.println(ans1 * ans2);
    }
}

// Archived