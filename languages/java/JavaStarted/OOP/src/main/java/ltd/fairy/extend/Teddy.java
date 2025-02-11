/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-10 21:58:22 UTC+08:00
 *****************************************************/
package ltd.fairy.extend;

import ltd.fairy.parent.Dog;

/**
 * @author Lionel Johnson
 */
public class Teddy extends Dog {

    public Teddy(String name) {
        super(name);
    }

    public void play() {
        System.out.println(super.getName() + "正在玩耍");
    }
}
