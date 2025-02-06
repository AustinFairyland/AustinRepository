/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 18:55:54 UTC+08:00
 *****************************************************/
package ltd.fairy.study;

/**
 * 自增/减运算符
 *
 * @author Lionel Johnson
 */
public class AutoAddSub {
    // a++, 先用后加, ++a, 先加后用, 同理
    public static void autoAdd() {

        int a = 10;
        System.out.println(a);  // 10
        a++;
        System.out.println(a);  // 11
        ++a;
        System.out.println(a);  // 12
    }

    public static void autoSub() {
        int a = 10;
        System.out.println(a);  // 10
        a--;
        System.out.println(a);  // 9
        --a;
        System.out.println(a);  // 8
    }

    public static void main(String[] args) {
        autoAdd();
        autoSub();
    }
}
