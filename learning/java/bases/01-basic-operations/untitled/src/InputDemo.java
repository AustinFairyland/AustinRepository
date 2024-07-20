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
public class InputDemo {
    public static void main(String[] args) {
        /*
         * 需求:
         * 从控制台输入一个人的3门学科, Java, Python, SQL 的成绩
         * 1. 计算Java和SQL的分数差
         * 2. 3门课程的平均分
         * */
        Scanner scanner = new Scanner(System.in);
        System.out.println("输入Java的成绩:");
        double scoreJava = scanner.nextDouble();
        System.out.println("输入Python的成绩:");
        double scorePython = scanner.nextDouble();
        System.out.println("输入法SQl的成绩:");
        double scoreSQL = scanner.nextDouble();

        double question1 = scoreJava - scoreSQL;
        double question2 = (scoreJava + scorePython + scoreSQL) / 3;
        System.out.println("Java课程和SQL课程的成绩差是: " + question1);
        System.out.println("3门课程的平均分是: " + question2);
    }
}