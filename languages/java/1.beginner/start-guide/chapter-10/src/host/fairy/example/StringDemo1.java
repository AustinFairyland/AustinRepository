/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-29 23:26:12 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class StringDemo1 {
    public static void main(String[] args) {
        String s1 = "abc";
        System.out.println(s1);

        String s2 = new String();  // ""
        System.out.println("###" + s2 + "###");

        String s3 = new String("abc");
        System.out.println(s3);

        char[] chars = {'a', 'b', 'c', 'd'};
        String s4 = new String(chars);
        System.out.println(s4);

        byte[] bytes = {97, 98, 99, 100, 'e'};
        String s5 = new String(bytes);
        System.out.println(s5);
    }
}
