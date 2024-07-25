/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 14:37:12 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class WhileLoop {
    public static void main(String[] args) {
        int i = 1, sum = 0;
        
        while (true) {
            System.out.println("While 循环.");
            if (i < 5) {
                i++;
            } else {
                break;
            }
        }
        
        // 由于上次循环, i的值已经发生变化, 这里重新赋值
        i = 1;

        while (i <= 100) {
            sum += i;
            i++;
        }
        System.out.println("1+2+3+...+100的和为: " + sum);
    }
}
