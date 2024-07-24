/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 16:52:34 UTC+08:00
 *****************************************************/

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class ForLoopDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入学生姓名: ");
        String name = scanner.next();
        double scoreSum = 0;
        for (int i = 1; i <= 5; i++) {
            System.out.print("请输入5门做功课中的第" + i + "门课的成绩为: ");
            double score = scanner.nextDouble();
            if (score < 0) {
                System.out.println("请输入正确的成绩");
                break;
            } else {
                scoreSum += score;
            }
        }
        System.out.println(name + "这5门功课的平均分是: " + (scoreSum / 5));
    }
}
