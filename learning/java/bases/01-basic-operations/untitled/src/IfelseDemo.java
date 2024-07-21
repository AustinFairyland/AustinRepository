/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-20 20:31:42 UTC+08:00
 *****************************************************/

import java.util.Random;
import java.util.Scanner;

/**
 * @author Lionel Johnson
 */
public class IfelseDemo {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int randomInt = random.nextInt(0, 10);
        System.out.println("幸运数字是: " + randomInt);

        System.out.println("请输入会员编号");
        if (scanner.hasNextInt()) {
            int vipNumber = scanner.nextInt();
            String vipStr = String.valueOf(vipNumber);

            if (vipStr.length() == 4) {
                char secChar = vipStr.charAt(1);
                int sceValue = Character.getNumericValue(secChar);
                if (sceValue == randomInt) {
                    System.out.println("恭喜你中奖了...");
                } else {
                    System.out.println("再接再厉...");
                }
            } else {
                System.out.println("请输入正确的会员编号.");
            }
        } else {
            System.out.println("输入的会员编号无效.");
        }

        scanner.close();
    }
}
