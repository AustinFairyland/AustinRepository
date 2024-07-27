/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-27 18:29:03 UTC+08:00
 *****************************************************/
package host.fairy.demo;

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class ArithmeticOperatorDemo1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入一个三位整数: ");
        int num = scanner.nextInt();
        
        int a = num % 10;
        int b = num / 10 % 10;
        int c = num / 100 % 10;

        System.out.println("个位数: " + a);
        System.out.println("十位数: " + b);
        System.out.println("百位数: " + c);
    }
}
