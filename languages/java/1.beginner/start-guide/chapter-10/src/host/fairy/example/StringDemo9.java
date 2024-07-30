/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 21:12:37 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.StringJoiner;

/**
 * @author Lionel Johnson
 */
public class StringDemo9 {
    public static void main(String[] args) {
        // string joiner
        StringJoiner stringJoiner = new StringJoiner(", ", "[", "]");
        String[] names = {"Lionel", "Johnson", "Fairy"};
        for (String name : names) {
            stringJoiner.add(name);
        }

        System.out.println(stringJoiner.toString());
        
    }
}
