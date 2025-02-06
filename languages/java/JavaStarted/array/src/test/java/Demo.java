/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 20:41:55 UTC+08:00
 *****************************************************/

import java.util.Arrays;

/**
 * @author Lionel Johnson
 */
public class Demo {
    private static int add(int[] ints) {
        int sum = 0;
        for (int num : ints) {
            sum += num;
        }

        return sum;
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        System.out.println(add(array));
        System.out.println(Arrays.stream(array).sum());
    }
}
