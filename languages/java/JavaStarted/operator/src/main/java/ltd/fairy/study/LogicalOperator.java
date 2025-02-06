/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 19:20:34 UTC+08:00
 *****************************************************/
package ltd.fairy.study;

/**
 * 逻辑运算符
 *
 * @author Lionel Johnson
 */
public class LogicalOperator {
    public static void main(String[] args) {
        /*
         * & 与, 全部为真则为真
         * | 或, 有一个为真则为真
         * ^ 异或, 相同为false, 不同为true
         * ! 非, 取反
         * */

        System.out.println(true & true); // true
        System.out.println(true & false); // false
        System.out.println(false & true); // false
        System.out.println(false & false); // false

        System.out.println(true | true); // true
        System.out.println(true | false); // true
        System.out.println(false | true); // true
        System.out.println(false | false); // false

        System.out.println(true ^ true); // false
        System.out.println(true ^ false); // true
        System.out.println(false ^ true); // true
        System.out.println(false ^ false); // false

        System.out.println(!true); // false
        System.out.println(!false); // true
        
    }
}
