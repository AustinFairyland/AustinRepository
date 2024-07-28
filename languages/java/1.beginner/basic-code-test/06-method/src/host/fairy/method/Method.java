/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-28 00:55:24 UTC+08:00
 *****************************************************/
package host.fairy.method;

/**
 * @author Lionel Johnson
 */
public class Method {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        playGame();
        getSum(5, 10);
        getCircleArea(2);
        System.out.println("Circle area: " + getCircleArea2(2));
        System.out.println("Circle area: " + getCircleArea2(7, 3.14));
    }

    public static void playGame() {
        System.out.println("Playing game...");
    }

    public static void getSum(int a, int b) {
        System.out.println("Sum: " + (a + b));
    }

    public static void getCircleArea(double radius) {
        System.out.println("Circle area: " + (Math.PI * Math.pow(radius, 2)));
    }

    public static double getCircleArea2(double radius) {
        return Math.PI * Math.pow(radius, 2);
    }
    
    public static double getCircleArea2(double radius, double pi) {
        return pi * Math.pow(radius, 2);
    }
}
