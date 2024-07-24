/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 15:56:40 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class DoWhileLoopDemo {
    public static void main(String[] args) {
        int count = 1;
        double c = 20;
        do {
            double f = (c * 9) / 5 + 32;
            System.out.println(c + "°C==" + f + "°F");
            c += 20;
            count++;
        } while (c < 250 && count <= 10);
    }
}
