/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 00:55:19 UTC+08:00
 *****************************************************/

import java.util.ArrayList;

/**
 * @author Lionel Johnson
 */
public class LoopArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();

        list.add(1);
        list.add(2);
        list.add(3);

        for (int element : list) {
            System.out.println(element);
        }
    }
}
