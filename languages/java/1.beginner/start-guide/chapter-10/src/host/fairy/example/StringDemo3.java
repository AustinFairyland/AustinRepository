/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 00:09:44 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class StringDemo3 {

    public static boolean userLogin(String username, String password) {
        return username.equals("admin") && password.equals("admin");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            System.out.print("Please enter your username:");
            String username = scanner.next();
            System.out.print("Please enter your password:");
            String password = scanner.next();

            boolean result = userLogin(username, password);

            if (result) {
                System.out.println("Login successful.");
                break;
            } else {
                System.out.println("Login failed, please try again.");
            }
        }
    }
}
