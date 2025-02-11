/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-10 21:46:27 UTC+08:00
 *****************************************************/
package ltd.fairy.parent;

/**
 * @author Lionel Johnson
 */
public class Animals {

    String name;

    private Animals() {
    }

    public Animals(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void eat(String foot) {
        System.out.println(this.name + "正在吃" + foot);
    }

    public void drink() {
        System.out.println(this.name + "正在喝水");
    }
}
