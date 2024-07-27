/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: @since: 2024-07-25 22:00:13 UTC+08:00
 *****************************************************/

import java.util.Arrays;

/**
 * @author Lionel Johnson
 */
public class ArrayDemo3 {
    public static void main(String[] args) {
        StringBuilder str = new StringBuilder();

        char[] chars = {'a', 'c', 'u', 'b', 'e', 'p', 'f', 'z'};
        for (char item : chars) {
            str.append(item).append(" ");
        }
        str.setLength(str.length() - 1);
        System.out.println("原来数组: " + str.toString());
        str.setLength(0);

        Arrays.sort(chars);
        for (char item : chars) {
            str.append(item).append(" ");
        }
        str.setLength(str.length() - 1);
        System.out.println("升序排序: " + str.toString());
        str.setLength(0);

        for (int i = chars.length - 1; i >= 0; i--) {
            str.append(chars[i]).append(" ");
        }
        str.setLength(str.length() - 1);
        System.out.println("降序排序: " + str.toString());
    }
}
