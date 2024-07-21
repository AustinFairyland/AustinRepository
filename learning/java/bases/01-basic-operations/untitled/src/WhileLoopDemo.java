/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 14:54:48 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class WhileLoopDemo {
    public static void main(String[] args) {
        int i = 1, sum = 0;
        while (i <= 100) {
            if ((i % 2) == 0) {
                sum += i;
            }
            i++;
        }
        System.out.println("100以内的偶数之和是: " + sum);

        // 使用等差数列求和公式
        int a = 2;
        int l = 100;
        int n = (l - a) / 2 + 1;
        int sum2 = n * (a + l) / 2;
        System.out.println("100以内的偶数之和是: " + sum2);
    }
}
