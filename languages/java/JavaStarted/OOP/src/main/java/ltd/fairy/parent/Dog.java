/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-10 21:53:30 UTC+08:00
 *****************************************************/
package ltd.fairy.parent;

/**
 * @author Lionel Johnson
 */
public class Dog extends Animals {

    public Dog(String name) {
        super(name);
    }

    public void lookHome() {
        System.out.println(this.name + "正在看家");
    }
}
