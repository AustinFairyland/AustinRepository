/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-28 00:27:24 UTC+08:00
 *****************************************************/
package host.fairy.demo;

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class ComparisonOperatorDemo1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("输入第一个数字: ");
        int a = scanner.nextInt();
        System.out.print("输入第二个数字: ");
        int b = scanner.nextInt();
        
        System.out.println((a > b));
    }
}
