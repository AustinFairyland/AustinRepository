/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-21 01:38:07 UTC+8
 ******************************************************/

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class IfelseDemo2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入是否为会员(y/n): ");
        String isVip = scanner.next();
        System.out.print("请输入购物金额: ");

        if (scanner.hasNextInt()) {
            int money = scanner.nextInt();
            double discount = 1;

            if (isVip.equals("y")) {
                if (money > 200) {
                    discount = 0.75;
                } else {
                    discount = 0.8;
                }
            } else {
                if (money > 100) {
                    discount = 0.9;
                }
            }

            System.out.println("实际付款: " + (money * discount));

        } else {
            System.out.println("请输入正确的金额.");
        }


    }
}
