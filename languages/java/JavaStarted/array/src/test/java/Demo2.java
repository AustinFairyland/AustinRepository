/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-06 21:06:28 UTC+08:00
 *****************************************************/

/**
 * @author Lionel Johnson
 */
public class Demo2 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9};

        int count = 0;
        for (int num : array) {
            if (num % 3 == 0) {
                count++;
            }
        }

        System.out.println("数组中能被3整除的元素个数是：" + count + "个");
    }
}
