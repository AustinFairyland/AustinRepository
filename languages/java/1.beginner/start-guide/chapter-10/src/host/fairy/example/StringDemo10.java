/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 21:26:28 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class StringDemo10 {
    public static String convertRomeNumber(String string) {
        return string.replace("10", "X")
                .replace("9", "IX")
                .replace("8", "VIII")
                .replace("7", "VII")
                .replace("6", "VI")
                .replace("5", "V")
                .replace("4", "IV")
                .replace("3", "III")
                .replace("2", "II")
                .replace("1", "I");
    }

    public static void main(String[] args) {
        String string = "asifqw1359ho9qhnbuq10owfha";
        System.out.println(convertRomeNumber(string));
    }
}
