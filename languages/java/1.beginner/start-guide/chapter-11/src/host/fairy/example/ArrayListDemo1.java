/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @since: 2024-07-30 22:16:04 UTC+08:00
 ****************************************************/
package host.fairy.example;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * @author Lionel Johnson
 */
public class ArrayListDemo1 {
    public static void main(String[] args) {
        ArrayList<String> strings = new ArrayList<>();
        
        strings.add("a");
        strings.add("b");

        System.out.println(strings);
        System.out.println(strings.size());
        
        strings.add(0, "1");
        System.out.println(strings);
        System.out.println(strings.get(1));
        
        strings.remove("a");  // 根据元素删除会返回 true 或者是 false, 如果没有这个元素则会返回 false
        strings.remove("c");
        System.out.println(strings);
        
        String index1 = strings.remove(1);  // 根据索引删除会返回被删除的元素
        System.out.println(index1);
        System.out.println(strings);
        
        strings.set(0, "2");
        System.out.println(strings);
    }
}
