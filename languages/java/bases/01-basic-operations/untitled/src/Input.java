/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-19 21:45:06 UTC+08:00
 ******************************************************/


import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class Input {

    /**
     * 输入 <br>
     *
     * @param args null
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入你的姓名:");
        String name = scanner.next();
        System.out.println("输入的姓名是: " + name);

        System.out.println("输入你的年龄:");
        int age = scanner.nextInt();
        System.out.println("输入的年龄是: " + age);

        System.out.println("输入你的工资:");
        double money = scanner.nextDouble();
        System.out.println("输入的工资是: " + money);
    }
}
