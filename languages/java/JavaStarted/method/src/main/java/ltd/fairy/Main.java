/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 22:24:46 UTC+08:00
 *****************************************************/
package ltd.fairy;

import ltd.fairy.study.Calculate;
import ltd.fairy.study.Method;

/**
 * @author Lionel Johnson
 */
public class Main {
    public static void main(String[] args) {
        Method.playGame();
        Method.girlFriendInfo();
        int result = Calculate.add(1, 2);
        System.out.println("1 + 2 = " + result);
    }
}
