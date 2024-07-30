/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 21:41:22 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class StringDemo11 {
    public static boolean loopCompare(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }

        String rotatedString = a;
        for (int i = 0; i < a.length(); i++) {
            rotatedString = rotatedString.substring(1) + rotatedString.charAt(0);
            if (rotatedString.equals(b)) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        String a = "abcde";
        String b = "cdeab";
        System.out.println(loopCompare(a, b));
    }
}
