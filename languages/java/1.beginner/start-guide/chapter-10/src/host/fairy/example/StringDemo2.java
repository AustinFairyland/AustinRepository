/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 00:02:54 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class StringDemo2 {
    public static void main(String[] args) {
        String s1 = "abc";
        String s2 = new String("abc");
        String s3 = "Abc";

        System.out.println((s1 == s2));
        // 字符串的比较
        System.out.println(s1.equals(s2));
        // 忽略大小写的比较
        System.out.println(s2.equalsIgnoreCase(s3));
    }
}
