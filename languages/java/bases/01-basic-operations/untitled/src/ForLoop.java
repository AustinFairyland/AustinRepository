/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 16:13:53 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class ForLoop {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 0; i <= 100; i++) {
            sum += i;
        }
        System.out.println("0-100的和为: " + sum);

        int[] ints = {1, 2, 3};
        for (int element : ints) {
            System.out.println(element);
        }
    }
}
