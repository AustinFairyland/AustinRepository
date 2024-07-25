/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 17:03:03 UTC+08:00
 *****************************************************/

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class ForLoopDemo2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入一个值: ");
        int val = scanner.nextInt();

        for (int i = 0, j = val; i <= val; i++, j--) {
            System.out.println(i + "+" + j + "=" + (i + j));
        }
    }
}
