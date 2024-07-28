/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-28 00:16:17 UTC+08:00
 *****************************************************/
package host.fairy.operator;

/**
 * @author Lionel Johnson
 */
public class LogicalOperator {
    public static void main(String[] args) {
        boolean a = true;
        boolean b = false;
        boolean c = true;
        boolean d = false;

        System.out.println("a && b = " + (a && b));
        System.out.println("a || b = " + (a || b));
        System.out.println("!(a && b) = " + !(a && b));
        System.out.println("!(a || b) = " + !(a || b));
        System.out.println("c && d = " + (c && d));
        System.out.println("c || d = " + (c || d));
        System.out.println("!(c && d) = " + !(c && d));
        System.out.println("!(c || d) = " + !(c || d));
        System.out.println("a ^ b = " + (a ^ b));
        System.out.println("!(a ^ b) = " + !(a ^ b));
        
    }
}
