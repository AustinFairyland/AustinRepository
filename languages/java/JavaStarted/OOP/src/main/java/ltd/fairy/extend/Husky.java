/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-10 21:57:00 UTC+08:00
 *****************************************************/
package ltd.fairy.extend;

import ltd.fairy.parent.Dog;

/**
 * @author Lionel Johnson
 */
public class Husky extends Dog {

    public Husky(String name) {
        super(name);
    }

    public void demolition() {
        System.out.println(super.getName() + "正在拆家");
    }
}
