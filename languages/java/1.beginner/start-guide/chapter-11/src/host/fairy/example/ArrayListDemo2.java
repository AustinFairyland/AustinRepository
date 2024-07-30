/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 22:29:04 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.ArrayList;
import java.util.StringJoiner;

/**
 * @author Lionel Johnson
 */
public class ArrayListDemo2 {
    public static <T> String refactor(ArrayList<T> arrayList) {
        StringJoiner stringJoiner = new StringJoiner(", ", "[", "]");

        for (T element : arrayList) {
            stringJoiner.add(element.toString());
        }
        return stringJoiner.toString();
    }
    
    public static void main(String[] args) {
        ArrayList<String> strings = new ArrayList<>();
        
        strings.add("a");
        strings.add("b");
        strings.add("c");

        System.out.println(refactor(strings));

        ArrayList<Integer> integers = new ArrayList<>();
        
        integers.add(1);
        integers.add(2);
        integers.add(3);
        System.out.println(refactor(integers));
    }
}
