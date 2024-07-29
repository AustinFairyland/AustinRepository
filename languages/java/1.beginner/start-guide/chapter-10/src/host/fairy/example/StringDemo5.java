/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 00:48:10 UTC+08:00
 ****************************************************/
package host.fairy.example;

/**
 * @author Lionel Johnson
 */
public class StringDemo5 {
    public static String arrayToString(int[] numbers) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        for (int i = 0; i < numbers.length; i++) {
            stringBuilder.append(numbers[i]);
            if (i < numbers.length - 1) {
                stringBuilder.append(", ");
            }
        }
        stringBuilder.append("]");
        return stringBuilder.toString();
    }

    public static String arrayToStringReverse(int[] numbers) {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("[");
        for (int i = numbers.length - 1; i >= 0; i--) {
            stringBuilder.append(numbers[i]);
            if (i > 0) {
                stringBuilder.append(", ");
            }
        }
        stringBuilder.append("]");
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println(arrayToString(numbers));
        System.out.println(arrayToStringReverse(numbers));
    }
}
