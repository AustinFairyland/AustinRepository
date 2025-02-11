/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-10 21:52:57 UTC+08:00
 *****************************************************/
package ltd.fairy.parent;

/**
 * @author Lionel Johnson
 */
public class Cat extends Animals {

    public Cat(String name) {
        super(name);
    }

    public void catchMouse() {
        System.out.println(this.name + "正在抓老鼠");
    }

    @Override
    public void eat(String foot) {
        System.out.println("Cat == eat");
        super.eat(foot);
    }
}
