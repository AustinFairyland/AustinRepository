/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-24 03:04:53 UTC+8
 ******************************************************/

import java.util.Arrays;
import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class ArraryDemo2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double[] moneyArray = new double[5];

        for (int i = 0; i < moneyArray.length; i++) {
            System.out.print("请输入第" + (i + 1) + "笔购物金额: ");
            double money = scanner.nextDouble();
            moneyArray[i] = money;
        }

        System.out.println("数组: " + Arrays.toString(moneyArray));
        System.out.println("序号\t金额(元)");
        double sum = 0;
        for (int i = 0; i < moneyArray.length; i++) {
            System.out.println((i + 1) + "\t" + moneyArray[i]);
            sum += moneyArray[i];
        }
        System.out.println("总金额\t" + sum);


    }
}