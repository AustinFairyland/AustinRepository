/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-27 13:54:22 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class Demo03 {
    public static void main(String[] args) {
        int number = 10;
        for (int i = 0; i < number; i++) {
            System.out.println("*".repeat(i + 1));
        }

        System.out.println("=".repeat(50));

        for (int i = 0; i < number; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println("=".repeat(50));

        for (int i = 0; i < number; i++) {
            for (int j = 0; j < (2 * i - 1); j++) {
                System.out.print("*");
            }
            System.out.println();
        }


        System.out.println("=".repeat(50));

        for (int i = 0; i < number; i++) {
            for (int j = (number - 1); j > i; j--) {
                System.out.print("*");
            }
            System.out.println();
        }


    }
}
