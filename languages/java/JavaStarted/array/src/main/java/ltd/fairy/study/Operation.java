/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 21:11:26 UTC+08:00
 *****************************************************/
package ltd.fairy.study;

import java.util.Arrays;

/**
 * @author Lionel Johnson
 */
public class Operation {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        System.out.println(array[0]);
        array[4] = 100;
        System.out.println(Arrays.toString(array));
    }
}
