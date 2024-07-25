/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-21 12:00:19 UTC+8
 ******************************************************/

import java.lang.reflect.Member;
import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class SwitchDemo2 {
    public static void main(String[] args) {
        Scanner scnaner = new Scanner(System.in);

        System.out.print("请输入消费金额: ");
        if (scnaner.hasNextDouble()) {
            double money = scnaner.nextDouble();
            System.out.println("是否参加换购:");
            System.out.println("1. 满50元, 加2元换购百事可乐饮料一瓶");
            System.out.println("2. 满100元, 加3元换购500ml可乐一瓶");
            System.out.println("3. 满100元, 加10元换购5KG面粉");
            System.out.println("4. 满200元, 加10元换购1个苏泊尔炒菜锅");
            System.out.println("5. 满200元, 加20元换购欧莱雅爽肤水一瓶");
            System.out.println("0. 不换购");
            System.out.print("请选择: ");
            if (scnaner.hasNextInt()) {
                int choise = scnaner.nextInt();
                switch (choise) {
                    case 1:
                        if (money < 50) {
                            System.out.println("消费金额小于50, 不能换购");
                            break;
                        }
                        System.out.println("本次消费总金额: " + (money + 2));
                        break;
                    case 2:
                        if (money < 100) {
                            System.out.println("金额小于100, 不能换购");
                            break;
                        }
                        System.out.println("本次消费总金额: " + (money + 3));
                        break;
                    case 3:
                        if (money < 100) {
                            System.out.println("金额小于100, 不能换购");
                            break;
                        }
                        System.out.println("本次消费总金额: " + (money + 10));
                        break;
                    case 4:
                        if (money < 200) {
                            System.out.println("金额小于200, 不能换购");
                            break;
                        }
                        System.out.println("本次消费总金额: " + (money + 10));
                        break;
                    case 5:
                        if (money < 200) {
                            System.out.println("金额小于200, 不能换购");
                            break;
                        }
                        System.out.println("本次消费总金额: " + (money + 20));
                        break;
                    default:
                        System.out.println("本次消费总金额: " + money);
                        break;
                }
            } else {
                System.out.println("输入失败");
            }
        } else {
            System.out.println("输入错误, 请重新输入.");
        }

    }
}