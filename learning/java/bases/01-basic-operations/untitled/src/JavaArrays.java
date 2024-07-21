/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-21 21:21:12 UTC+08:00
 *****************************************************/

import java.util.Arrays;

/**
 * @author Lionel Johnson
 */
public class JavaArrays {
    public static void main(String[] args) {
        // 声明一个只能放 int 的数组
        int[] ints;
        ints = new int[5];  // 设置数组里最大有5个成员
        // 给数组中的元素赋值
        ints[0] = 1;
        ints[1] = 2;
        ints[2] = 3;
        ints[3] = 4;
        ints[4] = 5;

        System.out.println(Arrays.toString(ints));  // 将数组转为字符串
        System.out.println(ints.length);  // 计算数组的元素个数
    }
}
