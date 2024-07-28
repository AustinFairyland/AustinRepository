/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-27 13:47:41 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class Demo02 {
    public static void main(String[] args) {
        int a = 10;
        String string = "*".repeat(a);
        for (int i = 0; i < a; i++) {
            System.out.println(string);
        }

        System.out.println("=".repeat(50));

        for (int i = 0; i < a; i++) {
            for (int j = 0; j < a; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}
