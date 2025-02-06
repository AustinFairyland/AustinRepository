/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 19:04:20 UTC+08:00
 *****************************************************/
package ltd.fairy.study;

/**
 * 赋值运算符
 *
 * @author Lionel Johnson
 */
public class AssignmentOperator {
    public static void main(String[] args) {
        int a = 10;
        a += 1;  // 等同于 a = (int)(a + 1)
        System.out.println(a);

        byte b = 10;
        b += 1;  // 等同于 b = (byte)(b + 1)
        System.out.println(b);
    }
}
