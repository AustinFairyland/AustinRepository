/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 15:24:26 UTC+08:00
 *****************************************************/

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class WhileLoopDemo2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("购物车结算");

        while (true) {
            System.out.println("*".repeat(20));
            System.out.println("请选择购买商品的编号");
            System.out.println("1. T恤, 2. 网球鞋, 3. 网球拍");
            System.out.println("*".repeat(20));
            System.out.print("请输入商品的编号: ");
            int id = scanner.nextInt();

            switch (id) {
                case 1:
                    System.out.println("T  恤 ->> ￥200.00");
                    break;
                case 2:
                    System.out.println("网球鞋 ->> ￥300.00");
                    break;
                case 3:
                    System.out.println("网球拍 ->> ￥300.00");
                    break;
                default:
                    break;
            }

            System.out.print("是否继续(y/n): ");
            String is_continue = scanner.next();

            if (is_continue.equals("y")) {
                continue;
            } else {
                break;
            }
        }

        scanner.close();
    }
}
