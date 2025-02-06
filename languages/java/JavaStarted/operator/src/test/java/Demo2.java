/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 19:29:56 UTC+08:00
 *****************************************************/


import java.util.Scanner;

/**
 * 短路逻辑运算符
 *
 * @author Lionel Johnson
 */
public class Demo2 {
    /**
     * 其中一个为6, 返回true, 如果他们的和是6的倍数, 输入true
     */
    private static boolean num6(int a, int b) {
        if (a == 6 || b == 6 || (a + b) % 6 == 0) {
            return true;
        } else {
            return false;
        }

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入两个整数: ");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println(num6(a, b));
    }
}
