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

        System.out.println("=".repeat(50));
        System.out.println(Arrays.toString(ints));  // 将数组转为字符串
        System.out.println(ints.length);  // 计算数组的元素个数
        System.out.println("=".repeat(50));
        System.out.println(Arrays.toString(args));

        /*
         * 数组属性: length -> 获取数组的长度
         * */
        // 分配空间并初始化赋值
        System.out.println("=".repeat(50));
        int[] ints1 = {1, 2, 3, 4, 5};
        // length 数值长度属性
        System.out.println("数组的长度: " + ints1.length);
        for (int item : ints1) {
            System.out.println(item);
        }

        /*
         * Arrays中的sort和toString方法
         *   sort: 对数组中的元素进行排序
         *   toString: 转换为字符串
         * */
        int[] ints2 = {8, 4, 2, 1, 23, 344, 12};
        Arrays.sort(ints2);
        System.out.println(Arrays.toString(ints2));


    }
}
