/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 00:15:54 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class StringDemo4 {

    public static void statistics(String string) {
        int upperCase = 0;
        int lowerCase = 0;
        int number = 0;
        int other = 0;

        for (int i = 0; i < string.length(); i++) {
            char ch = string.charAt(i);
            if (Character.isUpperCase(ch)) {
                upperCase++;
            } else if (Character.isLowerCase(ch)) {
                lowerCase++;
            } else if (Character.isDigit(ch)) {
                number++;
            } else {
                other++;
            }
        }

        System.out.println("The number of uppercase letters is " + upperCase);
        System.out.println("The number of lowercase letters is " + lowerCase);
        System.out.println("The number of numbers is " + number);
        System.out.println("The number of other characters is " + other);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Please enter a string:");
        String string = scanner.next();

        // 获取字符串中的索引
        System.out.println("The first character is " + string.charAt(0));
        // 获取字符的长度
        System.out.println("The length of the string is " + string.length());
        // 统计字符串中的字符个数
        statistics(string);
    }
}
