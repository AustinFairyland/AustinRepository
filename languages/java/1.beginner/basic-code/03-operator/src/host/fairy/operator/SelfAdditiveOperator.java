/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-27 22:06:44 UTC+08:00
 *****************************************************/
package host.fairy.operator;

/**
 * @author Lionel Johnson
 */
public class SelfAdditiveOperator {
    public static void main(String[] args) {
        // ++, --
        int a = 10;
        System.out.println(a);
        a++;
        System.out.println(a);
        ++a;
        System.out.println(a);
        a--;
        System.out.println(a);
        --a;
        System.out.println(a);
        
        int aAdd = a++;  // 先赋值再加1
        int adda = ++a;  // 先加1再赋值
        System.out.println(aAdd);
        System.out.println(adda);

    }
}
