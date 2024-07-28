/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-27 17:59:38 UTC+08:00
 *****************************************************/
package host.fairy.operator;

/**
 * @author Lionel Johnson
 */
public class ArithmeticOperator {
    public static void main(String[] args) {
        /*
         * 1. 整数参与计算, 结果也是整数
         * 2. 小数参与计算, 结果是有可能不精准的
         * */
        // 加法
        System.out.println(1 + 1);
        // 减法
        System.out.println(2 - 1);
        // 乘法
        System.out.println(2 * 2);

        // 如果有小数进行计算, 结果是有可能不精确的
        System.out.println(1.0 + 1.01);  // 2.01
        System.out.println(1.1 + 1.01);  // 2.1100000000000003
        System.out.println(1.7 - 0.21);
        System.out.println(2.8 * 3.01);

        // 除法
        System.out.println(10 / 2);  // 5
        System.out.println(10 / 3);  // 3
        System.out.println(10.0 / 3);  // 3.3333333333333335

        // 取模
        System.out.println(10 % 2);  // 0
        System.out.println(10 % 3);  // 1
        

    }
}
