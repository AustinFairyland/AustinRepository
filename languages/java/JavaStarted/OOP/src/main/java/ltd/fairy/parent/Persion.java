/*****************************************************
 * @software: IntelliJ IDEA
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-02-07 01:25:28 UTC+08:00
 *****************************************************/
package ltd.fairy.parent;

/**
 * @author Lionel Johnson
 */
public class Persion {
    protected String name;
    protected int age;

    private Persion() {
    }

    public Persion(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String eat(String food) {
        return this.name + "正在吃" + food;
    }

    public void sleep() {
        System.out.println(this.name + "正在睡觉");
    }
}
