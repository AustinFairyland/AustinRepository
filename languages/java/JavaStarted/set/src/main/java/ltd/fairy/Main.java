/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 00:38:07 UTC+08:00
 *****************************************************/
package ltd.fairy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringJoiner;

/**
 * @author Lionel Johnson
 */
public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Hello");
        list.add("World");

        System.out.println(list.size());

        System.out.println(String.join(",", list));
    }
}
