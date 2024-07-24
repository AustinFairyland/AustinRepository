/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-24 02:51:08 UTC+8
 ******************************************************/

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class ArraryDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] array = {8, 4, 2, 1, 23, 344, 12};
        int sum = 0;
        for (int i : array) {
            System.out.println("数组元素: " + i);
            sum += i;
        }
        System.out.println("数组元素之和: " + sum);

        System.out.print("请输入一个数: ");
        int num = scanner.nextInt();
        boolean flag = false;
        for (int i : array) {
            if (num == i) {
                flag = true;
                break;
            }
        }
        System.out.println(flag ? "输入的元素在数组中" : "输入的元素不在数组中");

    }
}