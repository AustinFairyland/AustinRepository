/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 14:48:29 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class DoWhileLoop {
    public static void main(String[] args) {
        int i = 1, sum = 0;
        do {
            sum += i;
            i++;
        } while (i <= 100);

        System.out.println("1-100的和为: " + sum);
    }
}
