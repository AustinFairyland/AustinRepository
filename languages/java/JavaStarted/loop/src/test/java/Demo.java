/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 19:51:56 UTC+08:00
 *****************************************************/

/**
 * 回文数
 *
 * @author Lionel Johnson
 */
public class Demo {
    private static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        String str = String.valueOf(x);
        String reverseStr = new StringBuilder(str).reverse().toString();
        return reverseStr.equals(str);
    }

    public static void main(String[] args) {
        int num = 1234321;
        System.out.println(isPalindrome(num));
    }
}
