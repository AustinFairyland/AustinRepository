/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 20:40:26 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class StringDemo8 {
    public static void main(String[] args) {
        // string builder
        StringBuilder stringBuilder = new StringBuilder("Hello, World!");
        stringBuilder.append("abc");

        System.out.println(stringBuilder);
        System.out.println(stringBuilder.toString());
        System.out.println(stringBuilder.length());
        System.out.println(stringBuilder.reverse());
    }
}
